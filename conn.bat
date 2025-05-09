@echo off
setlocal enabledelayedexpansion

for /f "tokens=1,2 delims==" %%A in (.\version2\env\.env.local) do (
    set %%A=%%B
)

echo Connecting to VM_Azure_Ubuntu %vm_user% on IP: %vm_ip_public%...
ssh %vm_user%@%vm_ip_public%

pause