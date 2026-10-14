import os
import sys
import subprocess

def get_base_dir():
    """Безопасное определение корня флешки с обходом песочницы macOS"""
    # Если запущен скомпилированный бинарник
    if getattr(sys, 'frozen', False):
        exe_dir = os.path.dirname(sys.executable)
        # Если мы внутри маковского бандла .app
        if "Contents/MacOS" in exe_dir:
            return os.path.abspath(os.path.join(exe_dir, "../../../.."))
        return exe_dir
    # Если запускаем просто как скрипт при отладке
    return os.path.dirname(os.path.abspath(__file__))

BASE_DIR = get_base_dir()

# Универсальные пути к интерпретатору Python внутри виртуального окружения на флешке
if sys.platform == "win32":
    python_executable = os.path.join(BASE_DIR, ".venv_windows", "Scripts", "python.exe")
    script_to_run = os.path.join(BASE_DIR, "src", "main.py")
    
    if os.path.exists(python_executable):
        subprocess.Popen([python_executable, script_to_run], cwd=BASE_DIR, creationflags=subprocess.CREATE_NO_WINDOW)

elif sys.platform == "darwin":
    # Путь к Python внутри маковского окружения на флешке
    python_executable = os.path.join(BASE_DIR, ".venv_mac", "bin", "python3")
    script_to_run = os.path.join(BASE_DIR, "src", "main.py")
    
    # 🍏 ВАЖНО ДЛЯ macOS: Если окружения еще нет, или запускаем напрямую
    if not os.path.exists(python_executable):
        # Если первого запуска не было и venv на флешке пустой, 
        # используем системный python3 мака, чтобы запустить стартовый скрипт настройки
        setup_script = os.path.join(BASE_DIR, "build_pure_pyinstaller_mac.command")
        subprocess.Popen(["/bin/bash", setup_script], cwd=BASE_DIR)
    else:
        # Если окружение .venv_mac уже готово, запускаем приложение напрямую БЕЗ ТЕРМИНАЛА!
        # Передаем переменные окружения, чтобы Flet знал, что он на десктопе Mac
        env = os.environ.copy()
        env["FLET_PLATFORM"] = "macos"
        subprocess.Popen([python_executable, script_to_run], cwd=BASE_DIR, env=env)
else:
    # Linux (для Юнуса)
    python_executable = os.path.join(BASE_DIR, ".venv_linux", "bin", "python3")
    script_to_run = os.path.join(BASE_DIR, "src", "main.py")
    if os.path.exists(python_executable):
        subprocess.Popen([python_executable, script_to_run], cwd=BASE_DIR)
