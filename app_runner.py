import os
import sys
import subprocess

# 1. Определяем корень проекта с учетом специфики бандла macOS (.app)
exe_dir = os.path.dirname(sys.executable)

if "Contents/MacOS" in exe_dir:
    # Если мы внутри скомпилированного .app на Маке, выходим на 4 уровня вверх к флешке
    BASE_DIR = os.path.abspath(os.path.join(exe_dir, "../../../.."))
else:
    # На Windows и Linux корень — это папка, где лежит сам exe/бинарник
    BASE_DIR = exe_dir

# 2. Определяем, на какой ОС мы запущены, и выбираем нужный скрипт
if sys.platform == "win32":
    script_path = os.path.join(BASE_DIR, "build_pure_pyinstaller_win.bat")
    # Молча будим батник Windows без открытия лишних консолей
    subprocess.Popen([script_path], cwd=BASE_DIR, creationflags=subprocess.CREATE_NO_WINDOW)
elif sys.platform == "darwin":
    script_path = os.path.join(BASE_DIR, "build_pure_pyinstaller_mac.command")
    # Молча запускаем bash-скрипт Мака
    subprocess.Popen(["bash", script_path], cwd=BASE_DIR)
else:
    script_path = os.path.join(BASE_DIR, "build_pure_pyinstaller_linux.sh")
    # Молча запускаем bash-скрипт Linux
    subprocess.Popen(["bash", script_path], cwd=BASE_DIR)
