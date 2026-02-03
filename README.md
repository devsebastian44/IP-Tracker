# IP-Tracker: Advanced Target Information Gatherer
> 📊 **[Ver Diagrama de Arquitectura y Flujo DevSecOps](./diagrams/arquitectura.md)**
> [!WARNING]
> **Ethical & Professional Use Statement**
> Este proyecto (`IP-Tracker`) ha sido desarrollado bajo un enfoque **estricto de Ciberseguridad Defensiva y Análisis de Inteligencia de Fuentes Abiertas (OSINT)**. Su propósito es exclusivo para investigación académica, auditorías autorizadas de seguridad y laboratorios de pruebas (`Red Teaming` controlado). El uso indebido para rastreo no autorizado o recolección maliciosa de datos es ilegal. Al utilizar este software, asumes la total responsabilidad de tus acciones y confirmas regirte mediante un código ético profesional.

---

## 🎯 Objetivo Técnico

**IP-Tracker** es una herramienta OSINT programática especializada en el rastreo, geolocalización y enriquecimiento de datos a partir de direcciones IPv4 e información asociada. 

Desarrollada para analistas de seguridad y consultores técnicos, la herramienta permite:
- Resolución y enriquecimiento masivo de direcciones de red.
- Consultas ágiles durante procesos de `Footprinting` dentro de fases tempranas del Pentesting.
- Integración en flujos de detección y recopilación manual.

---

## 🏛️ Arquitectura del Repositorio (DevSecOps)

Este repositorio ha sido estructurado bajo estándares **DevSecOps**, asegurando modularidad, separación de responsabilidades e integración segura:

```
IP-Tracker/
├── src/                  # Código fuente principal (Aplicación/Core)
├── scripts/              # Automatizaciones DevSecOps (Deploy local, sanitización)
├── tests/                # [GitLab] Pruebas unitarias y de integración (CI/CD)
├── docs/                 # Documentación técnica y diagramas arquitectónicos
├── .gitlab-ci.yml        # Pipeline DevSecOps (Linting, Unit Testing y SAST)
├── .gitignore            # Filtros de seguridad para evitar fuga de credenciales/artefactos
└── README.md             # Esta documentación base
```

> [!NOTE]
> **Separación de Entornos (Public / Private Strategy)**
> El código mantenido dentro de este repositorio de GitHub constituye la **versión pública y sanitizada** (orientada a portafolio profesional y auditoría externa).
>
> El entorno de desarrollo core y validación integral se mantiene de manera **privada en GitLab**, donde se operan: configuraciones críticas, rutinas de carga/payloads, infraestructura de dependencias y analítica estática, actuando este siempre como la `Source of Truth` (Fuente de Verdad).

---

## 🔄 Flujo de Trabajo (GitLab -> GitHub) & Automatización de Emisión (`publish_public.ps1`)

Para garantizar que el entorno público (GitHub) nunca exponga configuraciones sensibles, rutinas de pruebas agresivas o CI confidencial, el proceso de sincronización es controlado e intermediado.

### La Función del script de Sanitización: `publish_public.ps1`
Se trata de una pieza de automatización de seguridad crítica que actúa de la siguiente forma:

1. **Aislamiento en Rama Pública**: En el entorno aislado (GitLab), el desarrollador invoca el script validando su local y generando una versión clon en una rama segura denominada `public`.
2. **Filtrado DevSecOps (Purga)**: En la rama temporal, el script depura toda la información operativa del laboratorio: elimina el código backend/ejecutor agresivo (`src/`), rutinas automatizadas de testing (`tests/`), variables/configuraciones (`configs/`), CI interna y scripts operacionales sensibles. 
3. **Control de Emisión Push Force**: Una vez validado localmente el paquete expurgable/sanitizado con sus respectivas documentaciones y vistas (`docs/`, `diagrams/`), ejecuta únicamente un envío forzado hacia el `Origin` destino: Este repositorio de GitHub. 
4. **Resilencia de Laboratorio**: Una vez emitido la versión estable exterior, la máquina retorna su estado intacto hacia la rama de trabajo `main` del Laboratorio.

---

## ⚙️ Requisitos para el Ambiente (Uso Controlado)

- **Distribución de Seguridad**: Linux (Kali Linux, Parrot OS, BlackArch) o entornos virtualizados sobre Ubuntu. Compatible con capas Android (Termux) adaptadas.
- **Runtime Envrionment**: Python 3.9 o superior.

---

## 🚀 Instalación Standard (Source)

Aprovisionamiento dentro del entorno OSINT de Laboratorio:

```bash
git clone https://github.com/Devsebastian44/IP-Tracker.git
cd IP-Tracker
```

---

## ▶️ Ejecución y Uso (Versión de Laboratorio)

*Nota: Requiere poseer el código fuente del paquete (obtenido a nivel privado en la estructura `src/`).*

```bash
# Una vez descargado desde la fuente segura o dentro del laboratorio
python3 src/tracker.py
```

---

## 📜 Licenciamiento e Implicatura

Este proyecto dispone de una licencia **Apache 2.0**. Puedes bifurcarlo, modificarlo y emplearlo libremente bajo finalidades estrictamente **educativas e investigativas**.

### End of Documentation