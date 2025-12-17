# 📋 TAREAS PENDIENTES - UNS-Kobetsu 1.0v

> **Generado:** 2025-12-17 | **Audit Score:** 65/100

---

## 🔴 CRÍTICO (Bloquea Producción)

### 1. Re-habilitar Autenticación en Endpoints Destructivos
**Prioridad:** INMEDIATA
**Archivos:**
- [ ] `backend/app/api/v1/kobetsu.py:164-168` - Descomentar `get_current_user` en `/delete-all`
- [ ] `backend/app/api/v1/factories.py:108-111` - Descomentar `get_current_user` en `/delete-all`
- [ ] `backend/app/api/v1/employees.py:218-221` - Descomentar `get_current_user` en `/delete-all`
- [ ] `backend/app/api/v1/imports.py:64,102,130,167,191,242` - Descomentar en todos los endpoints

**Acción adicional:** Agregar `require_role("admin")` a endpoints delete-all

### 2. Regenerar JWT Secret Key
**Prioridad:** INMEDIATA
**Archivo:** `backend/app/core/config.py:52`
```bash
# Generar nueva clave:
openssl rand -hex 32
```
- [ ] Reemplazar valor hardcodeado por variable de entorno
- [ ] Actualizar `.env.example` con instrucciones

### 3. Habilitar Rate Limiting
**Prioridad:** INMEDIATA
**Archivo:** `backend/app/main.py:75-77`
- [ ] Descomentar `app.state.limiter = limiter`
- [ ] Descomentar `app.add_exception_handler(RateLimitExceeded, ...)`

### 4. Corregir Docker Base Images
**Prioridad:** INMEDIATA
**Archivos:**
- [ ] `backend/Dockerfile:1` - Cambiar `python:3.14-slim` → `python:3.11-slim`
- [ ] `frontend/Dockerfile:1` - Cambiar `node:25-alpine` → `node:20-alpine`

### 5. Asegurar Frontend Dockerfile
**Prioridad:** INMEDIATA
**Archivo:** `frontend/Dockerfile`
- [ ] Eliminar `chmod 777` (línea 18)
- [ ] Agregar usuario no-root
- [ ] Cambiar a build de producción (no `npm run dev`)

---

## 🟠 ALTA PRIORIDAD (Arreglar en 1 semana)

### 6. Restaurar Indexes Eliminados
**Archivo:** Crear nueva migración `006_restore_performance_indexes.py`
- [ ] `ix_kobetsu_status_dates`
- [ ] `ix_kobetsu_factory_status`
- [ ] `ix_kobetsu_created_at`
- [ ] `ix_employees_status_visa` (partial index)
- [ ] `ix_factory_lines_active` (partial index)

### 7. Corregir N+1 Query en Factory List
**Archivo:** `backend/app/api/v1/factories.py:79-98`
- [ ] Reemplazar loop de queries por subqueries/window functions
- [ ] Benchmark antes/después

### 8. Implementar Redis Caching
**Archivos:**
- [ ] Crear `backend/app/core/cache.py`
- [ ] Agregar cache decorator
- [ ] Cachear `/kobetsu/stats` (TTL: 60s)
- [ ] Cachear `/factories/dropdown/*` (TTL: 300s)

### 9. Proteger Registro de Usuarios
**Archivo:** `backend/app/api/v1/auth.py:184-230`
- [ ] Agregar verificación de email
- [ ] O requerir aprobación de admin
- [ ] O eliminar endpoint público

### 10. Corregir localStorage SSR
**Archivo:** `frontend/lib/api.ts:57,77,97`
- [ ] Envolver en `typeof window !== 'undefined'`
- [ ] O usar hook client-side only

---

## 🟡 MEDIA PRIORIDAD (Arreglar en 1 mes)

### 11. Dividir Archivos Grandes
- [ ] `backend/app/api/v1/kobetsu.py` (1,590 líneas) → kobetsu_crud.py, kobetsu_employees.py, kobetsu_documents.py
- [ ] `backend/app/api/v1/documents.py` (1,735 líneas) → Dividir por tipo de documento
- [ ] `frontend/components/kobetsu/KobetsuForm.tsx` (972 líneas) → Extraer secciones

### 12. Eliminar Tipos `any` en Frontend
**Archivos afectados:**
- [ ] `frontend/app/page.tsx:237,264,368`
- [ ] `frontend/app/kobetsu/create/page.tsx:33,45-46`
- [ ] `frontend/app/kobetsu/[id]/page.tsx:340`
- [ ] `frontend/components/kobetsu/KobetsuForm.tsx:241`

### 13. Agregar React.memo a Componentes
- [ ] `frontend/components/kobetsu/KobetsuTable.tsx`
- [ ] `frontend/components/kobetsu/KobetsuStats.tsx`
- [ ] Crear ContractRow como componente memoizado

### 14. Estandarizar Respuestas de Error
**Objetivo:** RFC 7807 compliance
- [ ] Crear schema `ProblemDetails`
- [ ] Actualizar exception handlers
- [ ] Documentar códigos de error

### 15. Agregar staleTime a useQuery
**Archivos:** Todos los componentes con useQuery
- [ ] kobetsu list: 30s
- [ ] stats: 60s
- [ ] factories dropdown: 300s

### 16. Implementar Background PDF Generation
**Archivo:** `backend/app/services/kobetsu_pdf_service.py`
- [ ] Usar FastAPI BackgroundTasks
- [ ] O implementar Celery
- [ ] Retornar status inmediato + polling

### 17. Agregar Logging Comprehensivo
**Archivos:**
- [ ] `backend/app/services/kobetsu_service.py` - Logger importado pero no usado
- [ ] `backend/app/services/import_service.py` - Sin logging
- [ ] Agregar audit trail para CRUD

### 18. Corregir Bare Except Clauses
- [ ] `backend/app/api/v1/health.py:85`
- [ ] `backend/app/api/v1/stats.py:253-254`
- [ ] Cambiar a `except Exception:` y loggear

### 19. Actualizar datetime.utcnow() Deprecado
- [ ] `backend/app/models/company.py:43-44`
- [ ] `backend/app/models/plant.py:34-35`
- [ ] Usar `datetime.now(timezone.utc)`

### 20. Agregar Constraints Faltantes en DB
- [ ] `ck_employee_status` - Validar valores de status
- [ ] `ck_employee_hire_date` - hire_date <= termination_date
- [ ] `ck_kobetsu_rates_positive` - Tarifas > 0

---

## 🟢 BAJA PRIORIDAD (Roadmap)

### 21. Accesibilidad (a11y)
- [ ] Agregar `scope` a headers de tablas
- [ ] Agregar `aria-label` a inputs sin label
- [ ] Agregar `role="region"` a stat cards

### 22. Consolidar Dual Hierarchy
- [ ] Decidir entre `factories` vs `companies/plants`
- [ ] Migrar datos
- [ ] Eliminar tablas redundantes

### 23. Agregar Tests End-to-End
- [ ] Configurar Playwright
- [ ] Tests de flujo completo de contrato
- [ ] Tests de autenticación

### 24. Implementar Audit Logging
- [ ] Crear tabla `audit_log`
- [ ] Trigger en cambios de contratos
- [ ] UI para ver historial

### 25. Configurar Kubernetes
- [ ] Crear manifests en `k8s/`
- [ ] Helm charts
- [ ] Horizontal Pod Autoscaler

### 26. Optimizar Bundle Size
- [ ] Lazy load chart.js
- [ ] Tree-shake heroicons
- [ ] Agregar bundle analyzer

### 27. Documentar OpenAPI Completamente
- [ ] Agregar response examples
- [ ] Documentar todos los error codes
- [ ] Agregar security scheme docs

### 28. Mover Hardcoded Values a Config
- [ ] Bank info en `documents.py:800-804`
- [ ] Employee-factory mapping en `import_service.py:26-73`
- [ ] Magic numbers (1095 días, rate multipliers)

---

## 📊 Resumen de Tareas

| Prioridad | Cantidad | Estimación |
|-----------|----------|------------|
| 🔴 Crítico | 5 | 1-2 días |
| 🟠 Alta | 5 | 1 semana |
| 🟡 Media | 10 | 2-4 semanas |
| 🟢 Baja | 8 | Roadmap |
| **Total** | **28** | - |

---

## ✅ Completado en Este Análisis

- [x] Análisis multi-agente completo (11 agentes)
- [x] Creación de tests de seguridad
- [x] Creación de tests de servicios
- [x] Creación de tests de frontend
- [x] Actualización de README con status
- [x] Creación de COMPREHENSIVE_AUDIT_REPORT.md

---

*Generado por Claude AI Multi-Agent Analysis System*
