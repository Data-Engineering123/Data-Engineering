@echo off
setlocal

REM Starts/checks NiFi and prints URL + latest generated login from logs
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0start_nifi_with_login.ps1"

endlocal
