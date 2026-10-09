@echo off
cd /d "%~dp0"
findstr /C:"YOUR_MONERO_ADDRESS" config.json >nul && (
    echo Open config.json and replace YOUR_MONERO_ADDRESS ^(both places^) with your Monero wallet address.
    pause
    exit /b 1
)
if not exist xmrig.exe (
    echo xmrig.exe not found. Put this file and config.json in the same folder as xmrig.exe.
    pause
    exit /b 1
)
xmrig.exe --config=config.json
pause
