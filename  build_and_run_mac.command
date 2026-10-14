#!/bin/bash
cd "$(dirname "$0")" || exit

clear
echo "======================================================"
echo "🍏 Silo-Core v3.0-RC1: Прямая сборка через PyInstaller..."
echo "======================================================"

# 1. Проверяем Python
if ! command -v python3 &> /dev/null; then
    echo "[ОШИБКА] На этом Mac не обнаружен Python 3!"
    read -p "Нажмите [Enter] для выхода..."
    exit 1
fi

# 2. Поднимаем venv
if [ ! -d ".venv_build_mac" ]; then
    echo "[1/4] Создаю окружение .venv_build_mac..."
    python3 -m venv .venv_build_mac
    source .venv_build_mac/bin/activate
    python3 -m pip install --upgrade pip > /dev/null
    echo "[2/4] Устанавливаю зависимости проекта и PyInstaller..."
    pip install -r requirements_mac.txt
    pip install pyinstaller  # Ставим чистый PyInstaller напрямую!
else
    source .venv_build_mac/bin/activate
fi

# 3. Компиляция напрямую через PyInstaller
echo "[3/4] 📦 Упаковка Flet-приложения через PyInstaller..."
# --windowed прячет консоль и делает нативный .app для Mac
pyinstaller --clean --onefile --windowed --name "SiloCoreSafe" src/main.py

if [ ! -d "dist/SiloCoreSafe.app" ] && [ ! -f "dist/SiloCoreSafe" ]; then
    echo "[КРИТИЧЕСКАЯ ОШИБКА] Сборка завершилась неудачей!"
    read -p "Нажмите [Enter] для выхода..."
    exit 1
fi

echo "[4/4] 🎉 Успешно! Скомпилированный файл лежит в папке dist/"
echo "🚀 Запускаю скомпилированный крипто-сейф..."

deactivate

# 4. Запуск готового бинарника
if [ -d "dist/SiloCoreSafe.app" ]; then
    open "dist/SiloCoreSafe.app"
else
    ./dist/SiloCoreSafe &
fi

sleep 3
