"""
Tests for Contract Service - Business Logic Layer.

Tests for contract renewal, date calculations, and validation logic.
"""
import pytest
from datetime import date, timedelta
from decimal import Decimal
from sqlalchemy.orm import Session

from app.models.kobetsu_keiyakusho import KobetsuKeiyakusho, KobetsuEmployee
from app.models.factory import Factory
from app.models.employee import Employee
from app.services.kobetsu_service import KobetsuService
from app.services.contract_logic_service import ContractLogicService


class TestContractNumberGeneration:
    """Test contract number generation."""

    def test_generate_contract_number_format(self, db: Session):
        """Test that contract numbers follow KOB-YYYYMM-XXXX format."""
        service = KobetsuService(db)
        number = service.generate_contract_number()

        assert number.startswith("KOB-")
        assert len(number) == 16  # KOB-YYYYMM-XXXX
        parts = number.split("-")
        assert len(parts) == 3
        assert len(parts[1]) == 6  # YYYYMM
        assert len(parts[2]) == 4  # XXXX

    def test_generate_unique_contract_numbers(self, db: Session):
        """Test that generated contract numbers are unique."""
        service = KobetsuService(db)
        numbers = [service.generate_contract_number() for _ in range(10)]
        assert len(numbers) == len(set(numbers))


class TestContractDateValidation:
    """Test contract date validation."""

    def test_start_date_before_end_date(self, db: Session):
        """Test that start date must be before end date."""
        service = ContractLogicService(db)

        # Valid dates
        assert service.validate_dates(
            date(2024, 1, 1),
            date(2024, 12, 31)
        ) is True

        # Invalid dates (start after end)
        assert service.validate_dates(
            date(2025, 1, 1),
            date(2024, 12, 31)
        ) is False

    def test_contract_period_calculation(self, db: Session):
        """Test calculation of contract period in months."""
        service = ContractLogicService(db)

        # 12 month contract
        months = service.calculate_period_months(
            date(2024, 1, 1),
            date(2024, 12, 31)
        )
        assert months == 12

        # 6 month contract
        months = service.calculate_period_months(
            date(2024, 1, 1),
            date(2024, 6, 30)
        )
        assert months == 6


class TestContractRenewal:
    """Test contract renewal logic."""

    def test_renew_creates_new_contract(
        self,
        db: Session,
        test_factory: Factory,
        test_employee: Employee
    ):
        """Test that renewal creates a new contract with new number."""
        service = KobetsuService(db)

        # Create original contract
        original = KobetsuKeiyakusho(
            factory_id=test_factory.id,
            contract_number="KOB-202401-0001",
            contract_date=date.today(),
            dispatch_start_date=date(2024, 1, 1),
            dispatch_end_date=date(2024, 12, 31),
            work_content="Test work content for contract",
            responsibility_level="Standard level",
            worksite_name="Test Site",
            worksite_address="Tokyo",
            status="active",
            number_of_workers=1
        )
        db.add(original)
        db.commit()

        # Create employee association
        emp_assoc = KobetsuEmployee(
            kobetsu_keiyakusho_id=original.id,
            employee_id=test_employee.id,
            hourly_rate=Decimal("1500")
        )
        db.add(emp_assoc)
        db.commit()

        # Renew
        renewal_data = {
            "dispatch_start_date": date(2025, 1, 1),
            "dispatch_end_date": date(2025, 12, 31)
        }

        renewed = service.renew(original.id, renewal_data)

        assert renewed is not None
        assert renewed.id != original.id
        assert renewed.contract_number != original.contract_number
        assert renewed.previous_contract_id == original.id
        assert renewed.status == "draft"


class TestContractDuplication:
    """Test contract duplication."""

    def test_duplicate_copies_all_fields(
        self,
        db: Session,
        test_factory: Factory
    ):
        """Test that duplication copies all required fields."""
        service = KobetsuService(db)

        # Create original
        original = KobetsuKeiyakusho(
            factory_id=test_factory.id,
            contract_number="KOB-202401-0001",
            contract_date=date.today(),
            dispatch_start_date=date(2024, 1, 1),
            dispatch_end_date=date(2024, 12, 31),
            work_content="Original work content",
            responsibility_level="Standard",
            worksite_name="Original Site",
            worksite_address="Original Address",
            organizational_unit="Manufacturing",
            supervisor_department="Production",
            supervisor_name="Manager Name",
            work_days=["Mon", "Tue", "Wed"],
            hourly_rate=Decimal("1500"),
            status="active",
            number_of_workers=1
        )
        db.add(original)
        db.commit()

        # Duplicate
        duplicate = service.duplicate(original.id)

        assert duplicate is not None
        assert duplicate.id != original.id
        assert duplicate.contract_number != original.contract_number
        assert duplicate.work_content == original.work_content
        assert duplicate.worksite_name == original.worksite_name
        assert duplicate.status == "draft"  # Always starts as draft


class TestContractStatusTransitions:
    """Test contract status transitions."""

    def test_activate_draft_contract(
        self,
        db: Session,
        test_factory: Factory
    ):
        """Test activating a draft contract."""
        service = KobetsuService(db)

        contract = KobetsuKeiyakusho(
            factory_id=test_factory.id,
            contract_number="KOB-202401-0001",
            contract_date=date.today(),
            dispatch_start_date=date.today(),
            dispatch_end_date=date.today() + timedelta(days=365),
            work_content="Test content",
            responsibility_level="Standard",
            worksite_name="Test Site",
            worksite_address="Address",
            status="draft",
            number_of_workers=1
        )
        db.add(contract)
        db.commit()

        activated = service.activate(contract.id)

        assert activated.status == "active"

    def test_cannot_activate_expired_contract(
        self,
        db: Session,
        test_factory: Factory
    ):
        """Test that expired contracts cannot be activated."""
        service = KobetsuService(db)

        contract = KobetsuKeiyakusho(
            factory_id=test_factory.id,
            contract_number="KOB-202301-0001",
            contract_date=date(2023, 1, 1),
            dispatch_start_date=date(2023, 1, 1),
            dispatch_end_date=date(2023, 12, 31),  # Expired
            work_content="Test content",
            responsibility_level="Standard",
            worksite_name="Test Site",
            worksite_address="Address",
            status="expired",
            number_of_workers=1
        )
        db.add(contract)
        db.commit()

        # Should not be able to activate expired contract
        with pytest.raises(Exception):
            service.activate(contract.id)


class TestLegalComplianceFields:
    """Test that all 16 legally required fields are validated."""

    def test_all_16_legal_fields_present(self):
        """
        Document the 16 legally required fields per Article 26.

        These fields must all be present in the KobetsuKeiyakusho model:
        1. work_content - 業務内容
        2. responsibility_level - 責任の程度
        3. worksite_name - 就業場所名
        4. worksite_address - 就業場所住所
        5. supervisor_* - 指揮命令者情報
        6. dispatch_start_date/dispatch_end_date - 派遣期間
        7. work_days - 就業日
        8. work_start_time/work_end_time - 就業時間
        9. break_time_minutes - 休憩時間
        10. safety_measures - 安全衛生
        11. haken_moto_complaint_contact - 派遣元苦情処理
        12. haken_saki_complaint_contact - 派遣先苦情処理
        13. termination_measures - 契約解除措置
        14. haken_moto_manager - 派遣元責任者
        15. haken_saki_manager - 派遣先責任者
        16. overtime_max_hours_* - 時間外労働
        """
        # Check that the model has all required attributes
        from app.models.kobetsu_keiyakusho import KobetsuKeiyakusho

        required_fields = [
            'work_content',
            'responsibility_level',
            'worksite_name',
            'worksite_address',
            'supervisor_name',
            'dispatch_start_date',
            'dispatch_end_date',
            'work_days',
            'work_start_time',
            'work_end_time',
            'break_time_minutes',
            'safety_measures',
            'haken_moto_complaint_contact',
            'haken_saki_complaint_contact',
            'termination_measures',
            'haken_moto_manager',
            'haken_saki_manager',
            'overtime_max_hours_day',
            'overtime_max_hours_month'
        ]

        model_fields = dir(KobetsuKeiyakusho)

        for field in required_fields:
            assert field in model_fields, (
                f"Missing legally required field: {field}"
            )


class TestRateCalculations:
    """Test hourly rate and overtime calculations."""

    def test_overtime_rate_default(self, db: Session):
        """Test default overtime rate calculation (1.25x)."""
        service = ContractLogicService(db)

        base_rate = Decimal("1500")
        overtime_rate = service.calculate_overtime_rate(base_rate)

        expected = Decimal("1875")  # 1500 * 1.25
        assert overtime_rate == expected

    def test_holiday_rate_calculation(self, db: Session):
        """Test holiday work rate calculation (1.35x)."""
        service = ContractLogicService(db)

        base_rate = Decimal("1500")
        holiday_rate = service.calculate_holiday_rate(base_rate)

        expected = Decimal("2025")  # 1500 * 1.35
        assert holiday_rate == expected

    def test_midnight_rate_calculation(self, db: Session):
        """Test midnight work rate calculation (1.25x + 0.25x)."""
        service = ContractLogicService(db)

        base_rate = Decimal("1500")
        midnight_rate = service.calculate_midnight_rate(base_rate)

        expected = Decimal("2250")  # 1500 * 1.5
        assert midnight_rate == expected
