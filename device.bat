@echo off
echo ================================
echo Restarting ADB server...
echo ================================

adb kill-server
adb start-server

echo.
echo Disconnecting old connections...
adb disconnect

echo.
echo Waiting...
timeout /t 3 /nobreak > nul

REM ====== SET PHONE IP MANUALLY ======
set DEVICE_IP=192.168.1.5
set ADB_PORT=5555

echo.
echo Switching ADB to TCP mode...
adb tcpip %ADB_PORT%

echo.
echo Connecting to device %DEVICE_IP%:%ADB_PORT% ...
adb connect %DEVICE_IP%:%ADB_PORT%

echo.
echo Connected devices:
adb devices

echo.
echo ================================
echo Done.
echo ================================
pause
