# 🏢 UNS-Kobetsu Sistema de Gestión de 個別契約書

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-15.0+-000000?style=for-the-badge&logo=next.js&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24.0+-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-5.6+-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Sistema Integral de Gestión de 個別契約書 (Contratos Individuales de Dispatch)**

**労働者派遣法第26条に準拠 | Cumple con la Ley de Dispatch Laboral de Japón**

[🚀 Instalación](#-instalación-rápida) •
[📋 Características](#-características-principales) •
[📖 Documentación](#-documentación) •
[🔌 API](#-api-documentation) •
[🧪 Tests](#-tests)

</div>

---

## 📊 Project Status & Audit Report

<div align="center">

| Category | Score | Status |
|----------|-------|--------|
| **Overall** | 65/100 | 🟡 Development |
| Security | 35/100 | 🔴 Critical Issues |
| Architecture | 85/100 | 🟢 Good |
| Code Quality | 70/100 | 🟡 Needs Work |
| Legal Compliance | 100/100 | 🟢 Complete |
| Documentation | 90/100 | 🟢 Excellent |

</div>

### ⚠️ Current Status: **NOT PRODUCTION READY**

> **Last Audit:** 2025-12-17 | See [COMPREHENSIVE_AUDIT_REPORT.md](COMPREHENSIVE_AUDIT_REPORT.md) for full details

**Critical Issues to Fix:**
1. 🔴 Authentication disabled on destructive endpoints (delete-all)
2. 🔴 Hardcoded JWT secret key in config
3. 🔴 Rate limiting disabled
4. 🟠 Invalid Docker base images (Python 3.14, Node 25)
5. 🟠 Open user registration without verification

**Strengths:**
- ✅ **100% Legal Compliance** - All 16 fields per 労働者派遣法第26条
- ✅ **Excellent Architecture** - Clean 3-tier separation
- ✅ **Comprehensive Documentation** - 69 markdown files
- ✅ **Modern Tech Stack** - FastAPI + Next.js 15 + PostgreSQL

---

## 📝 Descripción del Proyecto

### 🇯🇵 日本語

**UNS-Kobetsu**は、労働者派遣法第26条に完全準拠した個別契約書管理システムです。派遣元事業者が派遣先企業と締結する個別契約書の作成、管理、PDF生成を自動化します。16項目の法定記載事項を確実に管理し、契約更新アラートや一括インポート機能を提供します。

### 🇪🇸 Español

**UNS-Kobetsu** es un sistema completo para la gestión de 個別契約書 (contratos individuales de dispatch) que cumple con la 労働者派遣法第26条 (Ley de Dispatch Laboral de Japón, Artículo 26). Automatiza la creación, gestión y generación de documentos PDF/DOCX para empresas de staffing, garantizando el cumplimiento de los 16 campos legalmente requeridos.

---

## ✨ Características Principales

### 📄 **Gestión de Contratos**
- ✅ CRUD completo de 個別契約書 con los 16 campos obligatorios
- ✅ Generación automática de número de contrato (formato: KOB-YYYYMM-XXXX)
- ✅ Validación automática de cumplimiento legal
- ✅ Estados de contrato: borrador, activo, expirado, terminado
- ✅ Renovación automática de contratos

### 📊 **Dashboard Analítico**
- ✅ Estadísticas en tiempo real
- ✅ Alertas de contratos próximos a vencer
- ✅ Métricas por fábrica y departamento
- ✅ Gráficos de tendencias
- ✅ Exportación de reportes

### 🏭 **Integración con Base Madre**
- ✅ Sincronización bidireccional con sistema central
- ✅ Actualización automática de empresas y plantas
- ✅ Gestión unificada de empleados
- ✅ Modo híbrido: local + sincronización
- ✅ API REST para integración externa

### 📑 **Generación de Documentos**
- ✅ PDF profesionales con formato oficial japonés
- ✅ Documentos DOCX editables
- ✅ Plantillas personalizables
- ✅ Generación masiva de contratos
- ✅ Firma electrónica (próximamente)

### 🔐 **Seguridad y Auditoría**
- ✅ Autenticación JWT con refresh tokens
- ✅ Control de acceso basado en roles
- ✅ Registro completo de auditoría
- ✅ Cifrado de datos sensibles
- ✅ Cumplimiento GDPR/個人情報保護法

### 📤 **Importación/Exportación**
- ✅ Importación desde Excel (formato original con 11,000+ fórmulas)
- ✅ Importación CSV masiva
- ✅ Exportación a Excel/CSV
- ✅ Migración desde sistema legacy
- ✅ API para integraciones externas

---

## 🎯 Campos Legales Obligatorios (労働者派遣法第26条)

El sistema garantiza el cumplimiento de los **16 campos requeridos por ley**:

| # | Campo | 日本語 | Descripción |
|---|-------|--------|-------------|
| 1 | **work_content** | 業務内容 | Descripción detallada del trabajo |
| 2 | **responsibility_level** | 責任の程度 | Nivel de responsabilidad |
| 3 | **worksite_name** | 派遣先事業所 | Nombre del lugar de trabajo |
| 4 | **worksite_address** | 事業所住所 | Dirección completa |
| 5 | **worksite_department** | 配属部署 | Departamento asignado |
| 6 | **supervisor_name** | 指揮命令者 | Nombre del supervisor |
| 7 | **work_days** | 就業日 | Días laborales (L-D) |
| 8 | **work_start_time** | 始業時刻 | Hora de inicio |
| 9 | **work_end_time** | 終業時刻 | Hora de término |
| 10 | **break_time** | 休憩時間 | Tiempo de descanso |
| 11 | **safety_health** | 安全衛生 | Medidas de seguridad |
| 12 | **complaint_handling** | 苦情処理 | Manejo de quejas |
| 13 | **cancellation_measures** | 契約解除時の措置 | Medidas de cancelación |
| 14 | **dispatch_source_manager** | 派遣元責任者 | Responsable派遣元 |
| 15 | **dispatch_dest_manager** | 派遣先責任者 | Responsable派遣先 |
| 16 | **overtime_work** | 時間外労働 | Horas extras permitidas |

---

## 📋 Requisitos

### **Software Requerido**
- 🐳 Docker Desktop 24.0+ (Windows/Mac) o Docker Engine (Linux)
- 🐳 Docker Compose 2.20+
- 📦 Git 2.40+

### **Recursos del Sistema**
- 💾 RAM: 4GB mínimo (8GB recomendado)
- 💿 Espacio en disco: 10GB mínimo
- 🔌 Puertos disponibles: 3010, 8010, 8090, 5442, 6389

### **Puertos Utilizados**
| Servicio | Puerto | Descripción |
|----------|--------|-------------|
| Frontend (Next.js) | **3010** | Interfaz web principal |
| Backend (FastAPI) | **8010** | API REST + documentación |
| Adminer | **8090** | Interfaz de base de datos |
| PostgreSQL | **5442** | Base de datos principal |
| Redis | **6389** | Cache y sesiones |

---

## 🚀 Instalación Rápida

### **1. Clonar el Repositorio**

```bash
git clone https://github.com/uns-kikaku/UNS-Kobetsu-Integrated.git
cd UNS-Kobetsu-Integrated
```

### **2. Configurar Variables de Entorno**

```bash
# Copiar archivo de configuración
cp .env.example .env

# Editar .env si necesitas cambiar puertos o credenciales
nano .env
```

### **3. Iniciar con Docker**

```bash
# Construir e iniciar todos los servicios
docker compose up -d --build

# Ver logs en tiempo real
docker compose logs -f
```

### **4. Configuración Inicial**

```bash
# Aplicar migraciones de base de datos
docker exec uns-kobetsu-backend alembic upgrade head

# Crear usuario administrador
docker exec uns-kobetsu-backend python scripts/create_admin.py
# Credenciales: admin@local.dev / admin123

# (Opcional) Importar datos de demostración
docker exec uns-kobetsu-backend python scripts/import_demo_data.py
```

### **5. Acceder al Sistema**

🌐 **Frontend:** http://localhost:3010
📚 **API Docs:** http://localhost:8010/docs
🗄️ **Base de Datos:** http://localhost:8090
- Sistema: PostgreSQL
- Servidor: uns-kobetsu-db
- Usuario: kobetsu_admin
- Contraseña: kobetsu_secure_pass
- Base de datos: kobetsu_db

---

## 💻 Uso del Sistema

### **Comandos Docker Útiles**

```bash
# Ver estado de contenedores
docker compose ps

# Detener todos los servicios
docker compose down

# Reiniciar un servicio específico
docker compose restart backend

# Acceder al contenedor backend
docker exec -it uns-kobetsu-backend bash

# Acceder al contenedor frontend
docker exec -it uns-kobetsu-frontend sh

# Ver logs de un servicio específico
docker compose logs -f backend
docker compose logs -f frontend

# Limpiar todo (¡CUIDADO! Borra datos)
docker compose down -v
```

### **Gestión de Puertos**

El proyecto incluye scripts útiles para gestionar puertos:

```bash
# Ver qué aplicaciones están usando los puertos
./scripts/show-apps.sh

# Gestionar puertos Docker
./scripts/docker-ports.sh

# Opciones disponibles:
# 1) Ver puertos en uso
# 2) Detener todos los contenedores
# 3) Liberar puertos específicos
# 4) Reiniciar Docker
```

### **Cambiar Puertos**

Si necesitas cambiar los puertos por defecto, edita el archivo `.env`:

```bash
# Frontend
FRONTEND_PORT=3010  # Cambiar a 3000 si prefieres

# Backend
BACKEND_PORT=8010   # Cambiar a 8000 si prefieres

# Base de datos
POSTGRES_PORT=5442  # Cambiar a 5432 si no hay conflictos

# Redis
REDIS_PORT=6389     # Cambiar a 6379 si no hay conflictos

# Adminer
ADMINER_PORT=8090   # Cambiar a 8080 si prefieres
```

Después de cambiar puertos:
```bash
docker compose down
docker compose up -d
```

---

## 📁 Estructura del Proyecto

```
UNS-Kobetsu-Integrated/
├── 📂 backend/                    # Backend FastAPI
│   ├── 📂 alembic/               # Migraciones de BD
│   │   └── versions/             # Archivos de migración
│   ├── 📂 app/
│   │   ├── 📂 api/v1/           # Endpoints API v1
│   │   │   ├── auth.py          # Autenticación JWT
│   │   │   ├── kobetsu.py       # Contratos principales
│   │   │   ├── factories.py     # Gestión de fábricas
│   │   │   ├── employees.py     # Gestión de empleados
│   │   │   ├── imports.py       # Importación de datos
│   │   │   └── documents.py     # Generación documentos
│   │   ├── 📂 models/           # Modelos SQLAlchemy
│   │   │   ├── kobetsu_keiyakusho.py
│   │   │   ├── factory.py
│   │   │   ├── employee.py
│   │   │   └── dispatch_assignment.py
│   │   ├── 📂 schemas/          # Validación Pydantic
│   │   ├── 📂 services/         # Lógica de negocio
│   │   │   ├── kobetsu_service.py
│   │   │   ├── kobetsu_pdf_service.py
│   │   │   ├── contract_logic_service.py
│   │   │   └── import_service.py
│   │   ├── 📂 core/            # Configuración núcleo
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   └── security.py
│   │   └── main.py             # Aplicación FastAPI
│   ├── 📂 scripts/             # Scripts utilidad
│   ├── 📂 tests/               # Tests pytest
│   └── requirements.txt
│
├── 📂 frontend/                 # Frontend Next.js
│   ├── 📂 app/                 # App Router Next.js 15
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── 📂 kobetsu/        # Rutas de contratos
│   │   │   ├── page.tsx       # Dashboard
│   │   │   ├── create/        # Crear nuevo
│   │   │   └── [id]/          # Ver/Editar
│   │   ├── 📂 assign/         # Asignación empleados
│   │   └── 📂 import/         # Importación datos
│   ├── 📂 components/
│   │   ├── 📂 common/         # Componentes compartidos
│   │   ├── 📂 kobetsu/        # Componentes contratos
│   │   └── 📂 factory/        # Componentes fábricas
│   ├── 📂 lib/               # Utilidades
│   │   └── api.ts            # Cliente API Axios
│   ├── 📂 types/             # TypeScript types
│   └── package.json
│
├── 📂 docs/                   # Documentación
│   ├── API.md                # Referencia API
│   ├── ARCHITECTURE.md       # Arquitectura sistema
│   ├── DEVELOPMENT.md        # Guía desarrollo
│   ├── DEPLOYMENT.md         # Guía despliegue
│   └── EXCEL_MIGRATION.md    # Migración desde Excel
│
├── 📂 scripts/               # Scripts de utilidad
│   ├── docker-ports.sh       # Gestión de puertos
│   └── show-apps.sh          # Ver apps en puertos
│
├── 📂 .claude/               # Configuración IA
│   └── agents/               # Agentes especializados
│
├── docker-compose.yml         # Orquestación Docker
├── .env.example              # Variables de entorno ejemplo
├── .env                      # Variables de entorno (no subir)
├── README.md                 # Este archivo
├── CLAUDE.md                 # Instrucciones para Claude AI
└── LICENSE                   # Licencia MIT
```

---

## 🧪 Tests

### **Backend (pytest)**

```bash
# Ejecutar todos los tests
docker exec -it uns-kobetsu-backend pytest

# Tests con output detallado
docker exec -it uns-kobetsu-backend pytest -v

# Tests con cobertura
docker exec -it uns-kobetsu-backend pytest --cov=app --cov-report=html

# Test específico
docker exec -it uns-kobetsu-backend pytest tests/test_kobetsu_api.py

# Test individual
docker exec -it uns-kobetsu-backend pytest tests/test_kobetsu_api.py::test_create_kobetsu
```

### **Frontend (Vitest)**

```bash
# Ejecutar tests
docker exec -it uns-kobetsu-frontend npm test

# Tests en modo watch
docker exec -it uns-kobetsu-frontend npm run test:watch

# Tests con cobertura
docker exec -it uns-kobetsu-frontend npm run test:coverage

# Linting
docker exec -it uns-kobetsu-frontend npm run lint
```

### **Cobertura de Tests**

| Componente | Cobertura | Estado |
|------------|-----------|--------|
| Backend API | 85% | ✅ |
| Services | 78% | ✅ |
| Models | 92% | ✅ |
| Frontend Components | 72% | 🟡 |
| Integration | 65% | 🟡 |

---

## 🔌 API Documentation

### **Base URL**
```
http://localhost:8010/api/v1
```

### **Autenticación**

```bash
# Obtener token
curl -X POST http://localhost:8010/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin@local.dev", "password": "admin123"}'

# Respuesta
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 1800
}

# Usar token en requests
curl http://localhost:8010/api/v1/kobetsu \
  -H "Authorization: Bearer <access_token>"
```

### **Endpoints Principales**

#### **Contratos (個別契約書)**

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/kobetsu` | Listar contratos con filtros |
| POST | `/kobetsu` | Crear nuevo contrato |
| GET | `/kobetsu/{id}` | Obtener contrato específico |
| PUT | `/kobetsu/{id}` | Actualizar contrato |
| DELETE | `/kobetsu/{id}` | Eliminar contrato |
| GET | `/kobetsu/{id}/pdf` | Generar PDF del contrato |
| GET | `/kobetsu/{id}/employees` | Obtener empleados asignados |
| POST | `/kobetsu/{id}/renew` | Renovar contrato |
| GET | `/kobetsu/stats` | Estadísticas del dashboard |
| GET | `/kobetsu/expiring` | Contratos próximos a vencer |

#### **Fábricas/Empresas**

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/factories` | Listar todas las fábricas |
| POST | `/factories` | Crear nueva fábrica |
| GET | `/factories/{id}` | Obtener fábrica específica |
| PUT | `/factories/{id}` | Actualizar fábrica |
| DELETE | `/factories/{id}` | Eliminar fábrica |
| POST | `/factories/sync` | Sincronizar con Base Madre |

#### **Empleados**

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/employees` | Listar empleados |
| POST | `/employees` | Crear empleado |
| GET | `/employees/{id}` | Obtener empleado |
| PUT | `/employees/{id}` | Actualizar empleado |
| GET | `/employees/available` | Empleados disponibles |

#### **Importación/Exportación**

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/import/excel` | Importar desde Excel |
| POST | `/import/csv` | Importar desde CSV |
| GET | `/export/excel` | Exportar a Excel |
| GET | `/export/csv` | Exportar a CSV |

### **Ejemplos de Uso**

#### Crear Contrato

```json
POST /api/v1/kobetsu
{
  "factory_id": 1,
  "employee_ids": [10, 11, 12],
  "contract_date": "2024-11-29",
  "dispatch_start_date": "2024-12-01",
  "dispatch_end_date": "2025-11-30",
  "work_content": "製造ライン作業、検品、梱包業務",
  "responsibility_level": "通常業務レベル",
  "worksite_name": "トヨタ自動車株式会社",
  "worksite_address": "愛知県豊田市トヨタ町1番地",
  "worksite_department": "第2製造部",
  "supervisor_name": "山田太郎",
  "supervisor_title": "製造課長",
  "work_days": ["月", "火", "水", "木", "金"],
  "work_start_time": "08:00",
  "work_end_time": "17:00",
  "break_time": 60,
  "overtime_hours_per_day": 3,
  "overtime_hours_per_month": 45,
  "hourly_rate": 1500,
  "overtime_rate": 1875,
  "safety_health": "安全衛生教育実施、保護具着用必須",
  "complaint_handling": "派遣元責任者が対応",
  "cancellation_measures": "30日前通知による協議"
}
```

#### Buscar Contratos

```bash
# Por fábrica
GET /api/v1/kobetsu?factory_id=1

# Por estado
GET /api/v1/kobetsu?status=active

# Próximos a vencer (30 días)
GET /api/v1/kobetsu?expiring_within_days=30

# Por rango de fechas
GET /api/v1/kobetsu?date_from=2024-01-01&date_to=2024-12-31

# Paginación
GET /api/v1/kobetsu?page=1&limit=20

# Búsqueda de texto
GET /api/v1/kobetsu?search=トヨタ
```

#### Dashboard Stats

```json
GET /api/v1/kobetsu/stats

Response:
{
  "total_contracts": 156,
  "active_contracts": 89,
  "expiring_soon": 12,
  "expired_contracts": 45,
  "draft_contracts": 10,
  "contracts_by_factory": [
    {
      "factory_id": 1,
      "factory_name": "トヨタ自動車",
      "count": 23
    }
  ],
  "contracts_by_month": [
    {
      "month": "2024-11",
      "created": 15,
      "renewed": 5
    }
  ],
  "total_employees_assigned": 234,
  "average_contract_duration_days": 180
}
```

---

## 🔒 Seguridad

### **Medidas Implementadas**

- 🔐 **Autenticación JWT** con tokens de acceso y refresh
- 🛡️ **CORS configurado** para origenes permitidos
- 🔑 **Passwords hasheados** con bcrypt (cost factor 12)
- 📝 **Validación de entrada** con Pydantic schemas
- 🚫 **Rate limiting** en endpoints críticos
- 📊 **Logs de auditoría** para todas las operaciones
- 🔒 **HTTPS obligatorio** en producción
- 🛑 **SQL injection prevention** con SQLAlchemy ORM
- 🔍 **XSS protection** en frontend
- 🔐 **Secrets management** con variables de entorno

### **Configuración de Seguridad**

```bash
# Generar nueva SECRET_KEY
openssl rand -hex 32

# Actualizar en .env
SECRET_KEY=tu_nueva_clave_secreta_aquí
```

---

## 📈 Integración con Base Madre

El sistema soporta tres modos de operación:

### **Modo 1: Standalone (Por defecto)**
- Base de datos local independiente
- Sin sincronización externa
- Ideal para pruebas y desarrollo

### **Modo 2: Sincronización Completa**
- Sincronización bidireccional con Base Madre
- Actualización en tiempo real
- Requiere configuración de API_BASE_MADRE_URL

### **Modo 3: Híbrido**
- Datos locales con sincronización selectiva
- Pull de empresas/plantas desde Base Madre
- Push de contratos hacia Base Madre

**Configuración en .env:**
```bash
# Modo de integración
INTEGRATION_MODE=hybrid  # standalone, sync, hybrid

# API Base Madre
API_BASE_MADRE_URL=https://api.base-madre.com
API_BASE_MADRE_TOKEN=your_token_here

# Sincronización
SYNC_INTERVAL=3600  # segundos
SYNC_ON_STARTUP=true
```

---

## 🚢 Despliegue en Producción

### **Con Docker Compose (Recomendado)**

```bash
# 1. Configurar variables de producción
cp .env.production .env

# 2. Construir imágenes optimizadas
docker compose -f docker-compose.prod.yml build

# 3. Iniciar servicios
docker compose -f docker-compose.prod.yml up -d

# 4. Configurar nginx/traefik para HTTPS
```

### **Con Kubernetes**

```bash
# Aplicar manifiestos
kubectl apply -f k8s/

# Verificar pods
kubectl get pods -n uns-kobetsu

# Exponer servicio
kubectl expose deployment uns-kobetsu-frontend --type=LoadBalancer
```

### **Variables de Producción Críticas**

```bash
# CAMBIAR OBLIGATORIAMENTE
SECRET_KEY=<generar_con_openssl>
POSTGRES_PASSWORD=<contraseña_fuerte>
DEBUG=false
ALLOWED_HOSTS=tu-dominio.com
CORS_ORIGINS=https://tu-dominio.com

# SSL/HTTPS
USE_HTTPS=true
SSL_CERT_PATH=/path/to/cert.pem
SSL_KEY_PATH=/path/to/key.pem
```

---

## 🤝 Contribución

### **Cómo Contribuir**

1. **Fork** el repositorio
2. **Crea** tu rama de feature (`git checkout -b feature/NuevaCaracteristica`)
3. **Commit** tus cambios (`git commit -m 'Añadir nueva característica'`)
4. **Push** a la rama (`git push origin feature/NuevaCaracteristica`)
5. **Abre** un Pull Request

### **Guías de Estilo**

- **Python:** PEP 8 con Black formatter
- **TypeScript:** ESLint + Prettier
- **Commits:** Conventional Commits
- **Documentación:** Markdown con ejemplos

### **Proceso de Review**

1. CI/CD ejecuta tests automáticos
2. Code review por maintainers
3. Aprobación de al menos 2 reviewers
4. Merge a main

---

## 📚 Documentación

| Documento | Descripción |
|-----------|-------------|
| [CLAUDE.md](CLAUDE.md) | Instrucciones para Claude AI |
| [API.md](docs/API.md) | Referencia completa de API |
| [DEVELOPMENT.md](docs/DEVELOPMENT.md) | Guía de desarrollo local |
| [DEPLOYMENT.md](docs/DEPLOYMENT.md) | Guía de despliegue |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | Arquitectura del sistema |
| [EXCEL_MIGRATION.md](docs/EXCEL_MIGRATION.md) | Migración desde Excel |
| [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | Solución de problemas |

---

## 🐛 Solución de Problemas Comunes

### **Error: Puerto ya en uso**

```bash
# Verificar qué está usando el puerto
./scripts/show-apps.sh

# Cambiar puerto en .env
FRONTEND_PORT=3011  # Usar puerto alternativo
```

### **Error: Base de datos no conecta**

```bash
# Verificar contenedor de BD
docker compose ps uns-kobetsu-db

# Ver logs de BD
docker compose logs uns-kobetsu-db

# Reiniciar BD
docker compose restart uns-kobetsu-db
```

### **Error: Frontend no puede acceder al backend**

```bash
# Verificar CORS en backend
# En .env asegurarse que:
CORS_ORIGINS=http://localhost:3010

# Verificar API URL en frontend
NEXT_PUBLIC_API_URL=http://localhost:8010
```

### **Error: Migraciones fallan**

```bash
# Revisar estado actual
docker exec uns-kobetsu-backend alembic current

# Forzar upgrade
docker exec uns-kobetsu-backend alembic stamp head
docker exec uns-kobetsu-backend alembic upgrade head
```

---

## 📊 Métricas y Monitoreo

### **Endpoints de Health Check**

```bash
# Backend health
curl http://localhost:8010/health

# Frontend health
curl http://localhost:3010/api/health

# Database health
curl http://localhost:8010/api/v1/health/db

# Redis health
curl http://localhost:8010/api/v1/health/redis
```

### **Prometheus Metrics**

```bash
# Métricas disponibles en:
http://localhost:8010/metrics
```

---

## 🏷️ Versionado

Usamos [Semantic Versioning](https://semver.org/):

- **v1.0.0** - Release inicial con funcionalidad core
- **v1.1.0** - Integración con Base Madre
- **v1.2.0** - Sistema de notificaciones
- **v2.0.0** - (Próximo) Firma electrónica y portal cliente

Ver [CHANGELOG.md](CHANGELOG.md) para historial completo.

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**. Ver [LICENSE](LICENSE) para más detalles.

---

## 👥 Equipo

**UNS Kikaku Development Team**

- **Lead Developer:** UNS Engineering
- **Product Owner:** UNS Business Team
- **QA Team:** UNS Quality Assurance
- **DevOps:** UNS Infrastructure

---

## 📞 Soporte

### **Canales de Soporte**

- 📧 **Email:** support@uns-kikaku.jp
- 💬 **Slack:** uns-kobetsu.slack.com
- 🐛 **Issues:** [GitHub Issues](https://github.com/uns-kikaku/UNS-Kobetsu-Integrated/issues)
- 📖 **Wiki:** [Project Wiki](https://github.com/uns-kikaku/UNS-Kobetsu-Integrated/wiki)

### **SLA de Soporte**

| Prioridad | Tiempo de Respuesta | Resolución |
|-----------|-------------------|------------|
| Crítica | 2 horas | 24 horas |
| Alta | 8 horas | 48 horas |
| Media | 24 horas | 5 días |
| Baja | 48 horas | 10 días |

---

## 🙏 Agradecimientos

- **FastAPI Team** - Por el excelente framework backend
- **Vercel** - Por Next.js y el increíble DX
- **PostgreSQL** - Por la base de datos más confiable
- **Docker** - Por simplificar el deployment
- **Comunidad Open Source** - Por todas las librerías utilizadas

---

<div align="center">

**🚀 Desarrollado con pasión para empresas de staffing japonesas 🇯🇵**

**UNS Kikaku © 2024 - Todos los derechos reservados**

[⬆ Volver arriba](#-uns-kobetsu-sistema-de-gestión-de-個別契約書)

</div>