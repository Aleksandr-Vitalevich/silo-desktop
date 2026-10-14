#!/bin/bash
# Автоматически определяем текущую папку проекта (на флешке)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE}" )" && pwd )"
cd "$SCRIPT_DIR"

clear
echo "======================================================"
echo "🍏 Silo-Core v3.0-RC1: Ручная сборка нативного macOS..."
echo "======================================================"

# 1. Проверяем и активируем локальное виртуальное окружение .venv на флешке
if [ ! -d ".venv" ]; then
    echo "📦 Окружение .venv не найдено. Создаю заново..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install --upgrade pip
    pip3 install -r requirements_mac.txt
    pip3 install pyinstaller
else
    source .venv/bin/activate
fi

echo "🔮 Локальное окружение активировано!"

# 2. Компилируем САМЫЙ ГЛАВНЫЙ ФАЙЛ проекта напрямую через PyInstaller
echo "📦 Начинаю компиляцию нативного Flet-приложения..."

# Указываем путь к твоему главному файлу (например, src/main.py или main.py в корне)
# Флаг --windowed убирает терминал, --onefile собирает в один файл
pyinstaller --clean --onefile --windowed --name "SiloCoreSafe" src/main.py

if [ ! -d "dist/SiloCoreSafe.app" ] && [ ! -f "dist/SiloCoreSafe" ]; then
    echo "❌ [ОШИБКА] Сборка PyInstaller завершилась неудачей!"
    read -p "Нажмите [Enter] для выхода..."
    exit 1
fi

echo "✅ [УСПЕХ] Сборка завершена! Твоё приложение создано в папке dist/"
echo "------------------------------------------------------"
echo "⚠️  Чтобы запустить приложение на Маке без ошибок карантина,"
echo "выполни в терминале команду:"
echo "xattr -cr dist/SiloCoreSafe.app"
echo "------------------------------------------------------"

# 3. Снимаем карантин автоматически, чтобы окно сразу открывалось!
xattr -cr dist/SiloCoreSafe.app 2>/dev/null

echo "🚀 Запускаю скомпилированный сейф..."
deactivate

# Открываем нативный .app Mac-пакет
open "dist/SiloCoreSafe.app"
