import flet as ft
from state import AppState
import os

def add_file_function(page: ft.Page):
    """Интерфейс добавления файлов через прямой ввод пути (ультра-KISS и скорость)"""
    page.title = "Silo-Core Меню добавления файлов"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.clean()
    
    page.window_width = 1920
    page.window_height = 1080
    page.theme_mode = ft.ThemeMode.DARK

    name_file = ft.TextField(label="Введите название файла в Сейфе")
    
    path_file = ft.TextField(
        label="Путь к файлу на компьютере", 
        hint_text="Вставьте путь к файлу"
    )

    def on_save_to_db_click(e):
        file_path_on_disk = path_file.value.strip()
        if file_path_on_disk.startswith("'") or file_path_on_disk.startswith('"'):
            file_path_on_disk = file_path_on_disk[1:-1]

        if not name_file.value.strip():
            page.add(ft.Text("Ошибка: Введите название файла!", color="red"))
            page.update()
            return
            
        if not file_path_on_disk or not os.path.exists(file_path_on_disk):
            page.add(ft.Text("Ошибка: Указанный файл не найден на диске!", color="red"))
            page.update()
            return

        try:
            with open(file_path_on_disk, "rb") as f:
                raw_bytes = f.read()
                
            from utils.security import encrypt_file
            master_password = AppState.master_password
            
            enc_file = encrypt_file(raw_bytes, master_password)
            
            from db_manager.work_with_personal_files import add_file
            res = add_file(name_file.value.strip(), enc_file)
            
            if res == "success":
                page.add(ft.Text("Файл успешно сохранен!", color="green"))
                name_file.value = ""
                path_file.value = ""
                page.update()
                
        except Exception as ex:
            page.add(ft.Text(f"Ошибка чтения/записи файла: {ex}", color="red"))
            page.update()

    def go_back(e):
        from view.files.files_interface import add_files_operation
        add_files_operation(page)

    confirm_add = ft.FilledButton(
        content=ft.Text("Сохранить данные"),
        on_click=on_save_to_db_click
    )
    
    btn_back = ft.FilledButton(
        content=ft.Text("Назад в меню"),
        on_click=go_back
    )
    page.add(
        ft.Column([
            name_file,
            path_file,
            confirm_add,
            btn_back
        ])
    )
    page.update()
