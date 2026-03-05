param(
    [switch]$OpenBrowser = $true
)

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$nifiCmd = Join-Path $projectRoot "nifi-2.7.2-bin\nifi-2.7.2\bin\nifi.cmd"
$nifiProperties = Join-Path $projectRoot "nifi-2.7.2-bin\nifi-2.7.2\conf\nifi.properties"
$nifiUrl = "http://localhost:8080/nifi"

function Set-PropertyValue {
    param(
        [string]$Content,
        [string]$Key,
        [string]$Value
    )

    $pattern = "(?m)^$([regex]::Escape($Key))=.*$"
    if ($Content -match $pattern) {
        return [regex]::Replace($Content, $pattern, "$Key=$Value")
    }
    return ($Content.TrimEnd() + "`r`n$Key=$Value`r`n")
}

function Set-NifiNoLoginMode {
    param([string]$PropertiesPath)

    if (-not (Test-Path $PropertiesPath)) {
        throw "NiFi properties file not found: $PropertiesPath"
    }

    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    $content = [System.IO.File]::ReadAllText($PropertiesPath)
    $updates = [ordered]@{
        "nifi.web.http.host" = "localhost"
        "nifi.web.http.port" = "8080"
        "nifi.web.https.host" = ""
        "nifi.web.https.port" = ""
        "nifi.remote.input.secure" = "false"
        "nifi.security.user.authorizer" = ""
        "nifi.security.user.login.identity.provider" = ""
        "nifi.security.allow.anonymous.authentication" = "true"
        "nifi.security.keystore" = ""
        "nifi.security.keystoreType" = ""
        "nifi.security.keystorePasswd" = ""
        "nifi.security.keyPasswd" = ""
        "nifi.security.truststore" = ""
        "nifi.security.truststoreType" = ""
        "nifi.security.truststorePasswd" = ""
    }

    foreach ($entry in $updates.GetEnumerator()) {
        $content = Set-PropertyValue -Content $content -Key $entry.Key -Value $entry.Value
    }

    [System.IO.File]::WriteAllText($PropertiesPath, $content, $utf8NoBom)
}

if (-not (Test-Path $nifiCmd)) {
    throw "NiFi startup script not found: $nifiCmd"
}

Set-NifiNoLoginMode -PropertiesPath $nifiProperties
Write-Host "Starting/checking NiFi (no-login HTTP mode)..." -ForegroundColor Cyan

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

Write-Host ""
Write-Host "NiFi is UP" -ForegroundColor Green
Write-Host "URL      : $nifiUrl"
Write-Host "Login    : Not required"

if ($OpenBrowser) {
    Start-Process $nifiUrl | Out-Null
}
