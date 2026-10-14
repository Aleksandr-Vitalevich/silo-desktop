#!/bin/bash
cd "$(dirname "$0")" || exit

clear
echo "======================================================"
echo "🐧 Silo-Core v3.0-RC1: Авто-сборка и запуск для Linux..."
echo "======================================================"

if ! command -v python3 &> /dev/null; then
    echo "[ОШИБКА] В системе не найден Python 3!"
    read -p "Нажмите [Enter] для выхода..."
    exit 1
fi

if [ ! -d ".venv_build_linux" ]; then
    echo "[1/4] Создаю окружение сборщика .venv_build_linux..."
    python3 -m venv .venv_build_linux
    source .venv_build_linux/bin/activate
    python3 -m pip install --upgrade pip > /dev/null
    echo "[2/4] Устанавливаю зависимости проекта и PyInstaller..."
    pip install -r requirements_linux.txt
    pip install pyinstaller flet-cli==1.0.3
else
    source .venv_build_linux/bin/activate
fi

echo "[3/4] 📦 Компиляция проекта под Linux..."
flet pack src/main.py --name "SiloCoreSafe" --onefile

if [ ! -f "dist/SiloCoreSafe" ]; then
    echo "[КРИТИЧЕСКАЯ ОШИБКА] Не удалось скомпилировать бинарник Linux!"
    read -p "Нажмите [Enter] для выхода..."
    exit 1
fi

echo "[4/4] 🎉 Сборка завершена! Бинарник в папке dist/"
echo "🚀 Запускаю скомпилированное приложение..."

deactivate
./dist/SiloCoreSafe &
sleep 3
