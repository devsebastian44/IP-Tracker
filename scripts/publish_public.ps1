# =============================================================================
# scripts/publish_public.ps1 - VERSIÓN IP-TRACKER (SENIOR)
# Sincronización Segura: GitLab (Completo) -> GitHub (Sanitizado/Docs)
# =============================================================================

Write-Host "[*] Iniciando sincronización profesional de IP-Tracker..." -ForegroundColor Cyan

# 1. Validaciones Iniciales
$currentBranch = git rev-parse --abbrev-ref HEAD
if ($currentBranch -ne "main") {
    Write-Host "[!] Error: Debes estar en 'main' para publicar." -ForegroundColor Red
    exit
}

if (git status --porcelain) {
    Write-Host "[!] Tienes cambios sin guardar. Haz commit antes de publicar." -ForegroundColor Yellow
    exit
}

# 2. Limpieza Local Previa
Write-Host "[*] Limpiando artefactos de análisis y temporales..." -ForegroundColor Yellow
Remove-Item -Path "results/", "Resultados/", "Resultados_Tracker/" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "*.txt", "*.log" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "src/__pycache__" -Recurse -Force -ErrorAction SilentlyContinue

# 3. Sincronización con Laboratorio Privado (GitLab)
Write-Host "[*] Asegurando estado en GitLab..."
git pull gitlab main --rebase
git push gitlab main

# 4. Estrategia de Rama Pública (Aislamiento de Seguridad)
Write-Host "[*] Creando release sanitizado en rama 'public'..."
git checkout -B public main

# 5. Filtrado de Archivos (MANTENER SOLO DOCS/DIAGRAMAS/README PARA GITHUB)
Write-Host "[*] Aplicando filtros de seguridad DevSecOps (Sanitización)..." -ForegroundColor Cyan

# Eliminamos el código funcional y herramientas del laboratorio
git rm -r --cached src/ -f 2>$null
git rm -r --cached scripts/ -f 2>$null
git rm -r --cached tests/ -f 2>$null
git rm -r --cached configs/ -f 2>$null
git rm --cached .gitlab-ci.yml -f 2>$null

# 6. Commit de Lanzamiento y Push a GitHub (origin)
git commit -m "docs: release update to public portfolio (architecture and documentation)" --allow-empty
Write-Host "[*] Subiendo a GitHub (origin)..." -ForegroundColor Green
git push origin public:main --force

# 7. Retorno Seguro al Entorno de Trabajo (GitLab/Main)
Write-Host "[*] Volviendo al Laboratorio (main)..."
git checkout main -f
git clean -fd 2>$null

Write-Host "[*] Portafolio en GitHub actualizado (Solo Docs) y Lab en GitLab protegido (Completo)" -ForegroundColor Green