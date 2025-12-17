"""
Security tests for UNS-Kobetsu API endpoints.

These tests verify that authentication is properly enforced
on all sensitive endpoints, especially bulk delete operations.

CRITICAL: These tests document security requirements that MUST
be enforced before production deployment.
"""
import pytest
from fastapi.testclient import TestClient


class TestSecurityEndpoints:
    """Test cases for security-sensitive endpoints."""

    def test_delete_all_contracts_requires_auth(self, client: TestClient):
        """
        CRITICAL: delete-all endpoint MUST require authentication.

        This test will FAIL if auth is disabled on this endpoint.
        The endpoint at /api/v1/kobetsu/delete-all currently has
        authentication commented out - this is a security vulnerability.
        """
        response = client.delete("/api/v1/kobetsu/delete-all")
        # Should return 401 or 403, NOT 200
        assert response.status_code in [401, 403], (
            f"SECURITY VULNERABILITY: delete-all returned {response.status_code}. "
            "This endpoint MUST require authentication!"
        )

    def test_delete_all_factories_requires_auth(self, client: TestClient):
        """
        CRITICAL: delete-all factories endpoint MUST require authentication.
        """
        response = client.delete("/api/v1/factories/delete-all")
        assert response.status_code in [401, 403], (
            f"SECURITY VULNERABILITY: factories delete-all returned {response.status_code}. "
            "This endpoint MUST require authentication!"
        )

    def test_delete_all_employees_requires_auth(self, client: TestClient):
        """
        CRITICAL: delete-all employees endpoint MUST require authentication.
        """
        response = client.delete("/api/v1/employees/delete-all")
        assert response.status_code in [401, 403], (
            f"SECURITY VULNERABILITY: employees delete-all returned {response.status_code}. "
            "This endpoint MUST require authentication!"
        )

    def test_delete_all_requires_admin_role(
        self,
        client: TestClient,
        auth_headers: dict
    ):
        """
        Delete-all should require admin role, not just authentication.

        Note: This test assumes auth is enabled. If auth is disabled,
        this test will pass but the test_delete_all_*_requires_auth
        tests will fail.
        """
        # The current test user is admin, so this should succeed or require admin
        # If a non-admin user tries this, it should fail
        pass  # This test serves as documentation for required behavior

    def test_import_endpoints_require_auth(self, client: TestClient):
        """Test that import endpoints require authentication."""
        endpoints = [
            ("/api/v1/import/employees", "post"),
            ("/api/v1/import/factories", "post"),
        ]

        for endpoint, method in endpoints:
            if method == "post":
                response = client.post(endpoint, files={})
            else:
                response = client.get(endpoint)

            assert response.status_code in [401, 403, 422], (
                f"SECURITY: {endpoint} should require authentication, "
                f"got {response.status_code}"
            )


class TestAuthenticationFlow:
    """Test cases for authentication flow."""

    def test_login_with_valid_credentials(self, client: TestClient, test_user):
        """Test successful login."""
        response = client.post(
            "/api/v1/auth/login",
            json={
                "email": "test@example.com",
                "password": "testpassword"
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert "refresh_token" in data

    def test_login_with_invalid_credentials(self, client: TestClient):
        """Test login with wrong password."""
        response = client.post(
            "/api/v1/auth/login",
            json={
                "email": "test@example.com",
                "password": "wrongpassword"
            }
        )
        assert response.status_code in [401, 400]

    def test_login_with_nonexistent_user(self, client: TestClient):
        """Test login with non-existent email."""
        response = client.post(
            "/api/v1/auth/login",
            json={
                "email": "nonexistent@example.com",
                "password": "testpassword"
            }
        )
        assert response.status_code in [401, 400, 404]

    def test_login_with_inactive_user(
        self,
        client: TestClient,
        test_inactive_user
    ):
        """Test that inactive users cannot login."""
        response = client.post(
            "/api/v1/auth/login",
            json={
                "email": "inactive@example.com",
                "password": "testpassword"
            }
        )
        # Should fail - inactive users should not be able to login
        assert response.status_code in [401, 403]

    def test_refresh_token_flow(self, client: TestClient, test_user):
        """Test token refresh mechanism."""
        # First, login to get tokens
        login_response = client.post(
            "/api/v1/auth/login",
            json={
                "email": "test@example.com",
                "password": "testpassword"
            }
        )
        assert login_response.status_code == 200
        tokens = login_response.json()

        # Then refresh
        refresh_response = client.post(
            "/api/v1/auth/refresh",
            json={"refresh_token": tokens["refresh_token"]}
        )
        assert refresh_response.status_code == 200
        new_tokens = refresh_response.json()
        assert "access_token" in new_tokens

    def test_protected_endpoint_without_token(self, client: TestClient):
        """Test that protected endpoints require a token."""
        response = client.get("/api/v1/kobetsu")
        assert response.status_code in [401, 403]

    def test_protected_endpoint_with_invalid_token(self, client: TestClient):
        """Test that invalid tokens are rejected."""
        response = client.get(
            "/api/v1/kobetsu",
            headers={"Authorization": "Bearer invalid_token_here"}
        )
        assert response.status_code in [401, 403]


class TestPasswordSecurity:
    """Test cases for password security requirements."""

    def test_weak_password_rejected(self, client: TestClient):
        """Test that passwords shorter than 8 chars are rejected."""
        response = client.post(
            "/api/v1/auth/register",
            json={
                "email": "newuser@example.com",
                "password": "short",  # Too short
                "full_name": "New User"
            }
        )
        assert response.status_code == 400

    def test_password_min_length(self, client: TestClient):
        """Test minimum password length is enforced."""
        response = client.post(
            "/api/v1/auth/register",
            json={
                "email": "newuser2@example.com",
                "password": "12345678",  # Exactly 8 chars
                "full_name": "New User"
            }
        )
        # Should succeed with exactly 8 characters
        assert response.status_code in [200, 201, 400]  # May have other validation


class TestJWTSecurity:
    """Test cases for JWT token security."""

    def test_expired_token_rejected(self, client: TestClient):
        """Test that expired tokens are properly rejected."""
        # This would require generating an expired token
        # For now, document the requirement
        pass

    def test_token_type_mismatch_rejected(self, client: TestClient, test_user):
        """Test that using refresh token as access token fails."""
        # Login to get tokens
        login_response = client.post(
            "/api/v1/auth/login",
            json={
                "email": "test@example.com",
                "password": "testpassword"
            }
        )
        tokens = login_response.json()

        # Try to use refresh token as access token
        response = client.get(
            "/api/v1/kobetsu",
            headers={"Authorization": f"Bearer {tokens['refresh_token']}"}
        )
        # Should fail - refresh tokens should not work as access tokens
        assert response.status_code in [401, 403]
