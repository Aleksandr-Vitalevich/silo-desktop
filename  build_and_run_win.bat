@echo off
chcp 65001 > nul
title Silo-Core: Авто-сборка и запуск [Windows]

echo ======================================================
echo 🛠️ Silo-Core v3.0-RC1: Автоматическая сборка приложения...
echo ======================================================

:: 1. Проверяем наличие установленного Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ОШИБКА] На этом компьютере не обнаружен Python!
    echo Пожалуйста, установите Python 3.10+ перед запуском.
    pause
    exit /b
)

:: 2. Создаем venv, если его нет
if not exist ".venv_build_win" (
    echo [1/4] Создаю изолированное окружение для сборки...
    python -m venv .venv_build_win
    call .venv_build_win\Scripts\activate.bat
    python -m pip install --upgrade pip >nul
    echo [2/4] Устанавливаю зависимости проекта и PyInstaller...
    pip install -r requirements_windows.txt
    pip install pyinstaller flet-cli==1.0.3
) else (
    call .venv_build_win\Scripts\activate.bat
)

:: 3. Накатываем компиляцию через flet pack (PyInstaller под капотом)
echo [3/4] 📦 Компиляция проекта в один автономный .exe файл...
flet pack src/main.py --name "SiloCoreSafe" --onefile --noconsole

if %errorlevel% neq 0 (
    echo [КРИТИЧЕСКАЯ ОШИБКА] Сборка завершилась неудачей!
    pause
    exit /b
)

echo [4/4] 🎉 Сборка успешно завершена! Исполняемый файл в папке dist/
echo 🚀 Запускаю скомпилированный крипто-сейф...

:: 4. Автоматически запускаем готовый бинарник
deactivate
start "" "dist\SiloCoreSafe.exe"
timeout /t 3 >nul
