@echo off
chcp 65001 > nul
title Silo-Core: Прямая сборка PyInstaller [Windows]

echo ======================================================
echo 🛠️ Silo-Core v3.0-RC1: Прямая сборка без утилит Flet...
echo ======================================================

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ОШИБКА] На этом ПК не обнаружен Python!
    pause
    exit /b
)

if not exist ".venv_build_win" (
    echo [1/4] Создаю изолированное окружение...
    python -m venv .venv_build_win
    call .venv_build_win\Scripts\activate.bat
    python -m pip install --upgrade pip >nul
    echo [2/4] Устанавливаю зависимости проекта и чистый PyInstaller...
    pip install -r requirements_windows.txt
    pip install pyinstaller
) else (
    call .venv_build_win\Scripts\activate.bat
)

echo [3/4] 📦 Компиляция через PyInstaller в один клик...
:: --noconsole прячет черное окно терминала на Windows
pyinstaller --clean --onefile --noconsole --name "SiloCoreSafe" src/main.py

if %errorlevel% neq 0 (
    echo [КРИТИЧЕСКАЯ ОШИБКА] Сборка завершилась неудачей!
    pause
    exit /b
)

echo [4/4] 🎉 Сборка завершена! Исполняемый файл в папке dist/
echo 🚀 Запускаю скомпилированный крипто-сейф...

deactivate
start "" "dist\SiloCoreSafe.exe"
timeout /t 3 >nul
