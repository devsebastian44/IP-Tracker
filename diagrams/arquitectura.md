# Arquitectura y Flujo DevSecOps: IP-Tracker

Este diagrama ilustra la separación estricta de entornos (Privado vs Público) y el proceso automatizado de sanitización para despliegues orientados a portafolio.

```mermaid
flowchart TD
    %% Definición de Estilos
    classDef gitlab fill:#fca326,stroke:#e24329,stroke-width:2px,color:#fff,font-weight:bold;
    classDef github fill:#181717,stroke:#fff,stroke-width:2px,color:#fff,font-weight:bold;
    classDef script fill:#20c997,stroke:#12b886,stroke-width:2px,color:#fff,font-weight:bold;

    subgraph Lab_Privado ["🦊 Entorno Privado (GitLab) - Source of Truth"]
        direction TB
        Dev[Desarrollo en 'main'] --> CI{Pipeline CI/CD}
        CI -->|Linting| Rev[Flake8]
        CI -->|Testing| Test[Pytest]
        CI -->|Seguridad| SAST[Bandit SAST]
        Rev & Test & SAST --> Ready[Código validado y seguro]
    end

    subgraph Automatizacion ["⚙️ Script DevSecOps (publish_public.ps1)"]
        direction TB
        Ready --> Trigger[Ejecución script manual]
        Trigger --> Branch[Creación de rama temporal 'public']
        Branch --> Purge[Purga de archivos sensibles:<br/>- tests/<br/>- .gitlab-ci.yml<br/>- scripts/ operacionales]
    end

    subgraph Portafolio_Publico ["🐙 Entorno Público (GitHub) - Sanitizado"]
        direction TB
        Purge -->|Push Forzado| PushOrigin[Subida a origin (GitHub)]
        PushOrigin --> DocsOnly[Exposición exclusiva de docs, diagramas y README]
    end

    %% Asignación de clases
    Lab_Privado:::gitlab
    Automatizacion:::script
    Portafolio_Publico:::github
```
