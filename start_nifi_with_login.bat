@echo off
setlocal

REM Starts/checks NiFi in no-login mode and prints URL
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0start_nifi_with_login.ps1"

endlocal
