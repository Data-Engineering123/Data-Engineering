param(
    [switch]$OpenBrowser = $true
)

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$nifiCmd = Join-Path $projectRoot "nifi-2.7.2-bin\nifi-2.7.2\bin\nifi.cmd"
$nifiLog = Join-Path $projectRoot "nifi-2.7.2-bin\nifi-2.7.2\logs\nifi-app.log"
$nifiUrl = "https://localhost:8443/nifi"

function Get-LatestGeneratedCredentials {
    param([string]$LogPath)

    if (-not (Test-Path $LogPath)) {
        return $null
    }

    $lines = Get-Content -Path $LogPath -Tail 12000 -ErrorAction SilentlyContinue
    $username = $null
    $password = $null

    foreach ($line in $lines) {
        if ($line -match 'Generated Username \[(.+?)\]') {
            $username = $Matches[1]
        }
        if ($line -match 'Generated Password \[(.+?)\]') {
            $password = $Matches[1]
        }
    }

    if ($username -or $password) {
        return [pscustomobject]@{
            Username = $username
            Password = $password
        }
    }

    return $null
}

if (-not (Test-Path $nifiCmd)) {
    throw "NiFi startup script not found: $nifiCmd"
}

Write-Host "Starting/checking NiFi..." -ForegroundColor Cyan

$statusOutput = & $nifiCmd status 2>&1 | Out-String
if ($statusOutput -match 'Status:\s+UP') {
    Write-Host "NiFi is already running." -ForegroundColor Yellow
}
else {
    & $nifiCmd start | Out-Host
}

$up = $false
$statusOutput = ""
for ($attempt = 1; $attempt -le 40; $attempt++) {
    Start-Sleep -Seconds 2
    $statusOutput = & $nifiCmd status 2>&1 | Out-String
    if ($statusOutput -match 'Status:\s+UP') {
        $up = $true
        break
    }
}

if (-not $up) {
    Write-Warning "NiFi did not report UP within timeout."
    Write-Host $statusOutput
    exit 1
}

$creds = Get-LatestGeneratedCredentials -LogPath $nifiLog

Write-Host ""
Write-Host "NiFi is UP" -ForegroundColor Green
Write-Host "URL      : $nifiUrl"

if ($creds) {
    Write-Host "Username : $($creds.Username)"
    Write-Host "Password : $($creds.Password)"
}
else {
    Write-Warning "Could not find generated credentials in nifi-app.log."
    Write-Host "If you set custom single-user credentials manually, use those values."
}

if ($OpenBrowser) {
    Start-Process $nifiUrl | Out-Null
}
