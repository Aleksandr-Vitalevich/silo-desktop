#!/bin/bash

# 1. Безопасно привязываем терминал к папке, где лежит сам скрипт
TARGET_DIR="$(dirname "$0")"
cd "$TARGET_DIR" || exit

clear
echo "======================================================"
echo "🐧 Silo-Core v3.0-RC1: Прямая сборка Linux (для Юнуса)..."
echo "======================================================"

# 2. Проверяем наличие Python 3
if ! command -v python3 &> /dev/null; then
    echo "[ОШИБКА] В системе не найден Python 3!"
    echo "Пожалуйста, установите его перед запуском."
    read -p "Нажмите [Enter] для выхода..."
    exit 1
fi

# 3. Разворачиваем venv для сборки
if [ ! -d ".venv_build_linux" ]; then
    echo "[1/4] Создаю окружение .venv_build_linux..."
    python3 -m venv .venv_build_linux
    source .venv_build_linux/bin/activate
    python3 -m pip install --upgrade pip > /dev/null
    echo "[2/4] Устанавливаю зависимости проекта и чистый PyInstaller..."
    pip install -r requirements_linux.txt
    pip install pyinstaller  # Ставим чистый PyInstaller напрямую!
else
    source .venv_build_linux/bin/activate
fi

# 4. Компиляция напрямую через PyInstaller
echo "[3/4] 📦 Упаковка Flet-приложения для Linux..."
pyinstaller --clean --onefile --name "SiloCoreSafe" src/main.py

if [ ! -f "dist/SiloCoreSafe" ]; then
    echo "[КРИТИЧЕСКАЯ ОШИБКА] Не удалось скомпилировать бинарник Linux!"
    read -p "Нажмите [Enter] для выхода..."
    exit 1
fi

echo "[4/4] 🎉 Успешно! Скомпилированный файл лежит в папке dist/"
echo "🚀 Запускаю скомпилированный крипто-сейф..."

deactivate

# 5. Автоматический запуск готового бинарника в фоне
./dist/SiloCoreSafe &

sleep 3
