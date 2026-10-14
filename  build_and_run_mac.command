#!/bin/bash
cd "$(dirname "$0")" || exit

clear
echo "======================================================"
echo "🍏 Silo-Core v3.0-RC1: Авто-сборка и запуск для macOS..."
echo "======================================================"

# 1. Проверяем Python3
if ! command -v python3 &> /dev/null; then
    echo "[ОШИБКА] На этом Mac не обнаружен установленный Python 3!"
    read -p "Нажмите [Enter] для выхода..."
    exit 1
fi

# 2. Поднимаем venv для сборки
if [ ! -d ".venv_build_mac" ]; then
    echo "[1/4] Создаю изолированное окружение для сборки на Mac..."
    python3 -m venv .venv_build_mac
    source .venv_build_mac/bin/activate
    python3 -m pip install --upgrade pip > /dev/null
    echo "[2/4] Устанавливаю зависимости проекта и PyInstaller..."
    pip install -r requirements_mac.txt
    pip install pyinstaller flet-cli==1.0.3
else
    source .venv_build_mac/bin/activate
fi

# 3. Компиляция проекта
echo "[3/4] 📦 Компиляция проекта в автономный пакет macOS..."
export FLET_PLATFORM="macos"
flet pack src/main.py --name "SiloCoreSafe" --onefile

if [ ! -d "dist/SiloCoreSafe.app" ] && [ ! -f "dist/SiloCoreSafe" ]; then
    echo "[КРИТИЧЕСКАЯ ОШИБКА] Сборка на Mac завершилась сбоем!"
    read -p "Нажмите [Enter] для выхода..."
    exit 1
fi

echo "[4/4] 🎉 Сборка успешно завершена! Пакет находится в папке dist/"
echo "🚀 Запускаю скомпилированный крипто-сейф..."

# 4. Отключаем окружение сборщика и запускаем готовое скомпилированное приложение
deactivate

if [ -d "dist/SiloCoreSafe.app" ]; then
    open "dist/SiloCoreSafe.app"
else
    ./dist/SiloCoreSafe &
fi

sleep 3
