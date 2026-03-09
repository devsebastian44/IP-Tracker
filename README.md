# IP-Tracker: Advanced Target Information Gatherer

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![GitLab](https://img.shields.io/badge/GitLab-Repository-orange?logo=gitlab)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![OSINT](https://img.shields.io/badge/Type-OSINT-informational)
![Educational](https://img.shields.io/badge/Purpose-Educational-blue)

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
├── src/                  # Código fuente principal (Core / Aplicación)
├── scripts/              # Automatizaciones DevSecOps (Sanitización)
├── tests/                # Pruebas unitarias y de integración (Excluido en GitHub)
├── docs/                 # Documentación técnica adicional
├── diagrams/             # Diagramas arquitectónicos (Mermaid/MD)
├── .gitlab-ci.yml        # Pipeline DevSecOps (GitLab only)
├── .gitignore            # Filtros de exclusión
├── LICENSE               # Licencia Apache 2.0
└── README.md             # Esta documentación base
```

## 🚀 Instalación y Acceso

> [!IMPORTANT]
> El repositorio completo con todo el código funcional está disponible en **GitLab** para acceso completo.

https://gitlab.com/group-cybersecurity-lab/IP-Tracker.git


---

## 🔄 Flujo de Trabajo (GitLab -> GitHub) & Automatización de Emisión (`publish_public.ps1`)

Para garantizar que el entorno público (GitHub) nunca exponga configuraciones sensibles, rutinas de pruebas agresivas o CI confidencial, el proceso de sincronización es controlado e intermediado.

### La Función del script de Sanitización: `publish_public.ps1`
Se trata de una pieza de automatización de seguridad crítica que actúa de la siguiente forma:

1. **Aislamiento en Rama Pública**: En el entorno aislado (GitLab), el desarrollador invoca el script validando su local y generando una versión clon en una rama segura denominada `public`.
2. **Filtrado DevSecOps (Purga)**: En la rama temporal, el script depura toda la información operativa del laboratorio: elimina rutinas automatizadas de testing (`tests/`), variables/configuraciones locales (`configs/` si existieran), la CI interna (`.gitlab-ci.yml`) y scripts operacionales sensibles.
3. **Control de Emisión Push Force**: Una vez validado localmente el paquete sanitizado con sus respectivas documentaciones y vistas (`src/`, `docs/`, `diagrams/`, `Img/`), ejecuta únicamente un envío forzado hacia el `Origin` destino: Este repositorio de GitHub.
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