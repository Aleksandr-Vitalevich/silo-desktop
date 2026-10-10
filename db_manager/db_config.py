import os
import sys

if getattr(sys, 'frozen', False):
    exe_dir = os.path.dirname(sys.executable)
    if "Contents/MacOS" in exe_dir:
        BASE_DIR = os.path.abspath(os.path.join(exe_dir, "../../../"))
    else:
        BASE_DIR = exe_dir
else:
    current_file_path = os.path.abspath(__file__)
    db_manager_dir = os.path.dirname(current_file_path)
    BASE_DIR = os.path.dirname(db_manager_dir)

DB_PATH = os.path.join(BASE_DIR, "silo.db")
