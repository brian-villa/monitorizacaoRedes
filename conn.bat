@echo off
setlocal enabledelayedexpansion

for /f "tokens=1,2 delims==" %%A in (env\.env.local) do (
    set %%A=%%B
)

echo Connecting to VM_Azure_Ubuntu %vm_user% on IP: %vm_ip_public%...
ssh %VM_USER%@%VM_IP%

pause