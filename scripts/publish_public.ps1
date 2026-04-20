# =============================================================================
# scripts/publish_public.ps1 - VERSIÓN IP-TRACKER (SENIOR)
# Sincronización Segura: GitLab (Completo) -> GitHub (Sanitizado/Docs)
# =============================================================================

Write-Host "[*] Iniciando sincronización profesional de IP-Tracker..." -ForegroundColor Cyan

# 1. Validaciones de Entorno y Remotos
Write-Host "[*] Validando configuración de Git..." -ForegroundColor Yellow

# Verificar si los remotos necesarios existen
$remotes = git remote
if ($remotes -notcontains "gitlab") {
    Write-Host "[!] Error: El remoto 'gitlab' (Privado) no está configurado." -ForegroundColor Red
    Write-Host "    Usa: git remote add gitlab <URL_GITLAB>" -ForegroundColor Gray
    exit 1
}

if ($remotes -notcontains "origin") {
    Write-Host "[!] Error: El remoto 'origin' (GitHub Público) no está configurado." -ForegroundColor Red
    Write-Host "    Usa: git remote add origin <URL_GITHUB>" -ForegroundColor Gray
    exit 1
}

# Verificar que los remotos no sean iguales
$gitlabUrl = git remote get-url gitlab
$githubUrl = git remote get-url origin

if ($gitlabUrl -eq $githubUrl) {
    Write-Host "[!] ERROR CRÍTICO: Los remotos 'gitlab' y 'origin' apuntan a la misma URL." -ForegroundColor Red
    Write-Host "    Esto causaría la pérdida de código en tu laboratorio privado." -ForegroundColor Yellow
    exit 1
}

# Verificar estado de la rama
$currentBranch = git rev-parse --abbrev-ref HEAD
if ($currentBranch -ne "main") {
    Write-Host "[!] Error: Debes estar en 'main' para publicar." -ForegroundColor Red
    exit 1
}

if (git status --porcelain) {
    Write-Host "[!] Tienes cambios sin guardar. Haz commit antes de publicar." -ForegroundColor Yellow
    exit 1
}

# 2. Limpieza Local Previa
Write-Host "[*] Limpiando artefactos de análisis y temporales..." -ForegroundColor Yellow
Remove-Item -Path "results/", "Resultados/", "Resultados_Tracker/" -Recurse -Force -ErrorAction SilentlyContinue 2>$null
Remove-Item -Path "*.txt", "*.log" -Force -ErrorAction SilentlyContinue 2>$null
Remove-Item -Path "src/__pycache__" -Recurse -Force -ErrorAction SilentlyContinue 2>$null

# 3. Sincronización con Laboratorio Privado (GitLab)
Write-Host "[*] Asegurando estado en GitLab (Privado)..."
git pull gitlab main --rebase
if ($LASTEXITCODE -ne 0) { Write-Host "[!] Fallo al sincronizar con GitLab." -ForegroundColor Red; exit 1 }
git push gitlab main

# 4. Estrategia de Rama Pública (Aislamiento de Seguridad)
Write-Host "[*] Creando release sanitizado en rama 'public'..."
if (git branch | Select-String "public") { git branch -D public }
git checkout -B public main

# 5. Filtrado de Archivos (MANTENER SOLO DOCS/DIAGRAMAS/README PARA GITHUB)
Write-Host "[*] Aplicando filtros de seguridad DevSecOps (Sanitización)..." -ForegroundColor Cyan

# Eliminamos el código funcional y herramientas del laboratorio
$foldersToRemove = @("src/", "scripts/", "tests/", "configs/")
foreach ($folder in $foldersToRemove) {
    git rm -r --cached $folder -f 2>$null
}
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