import flet as ft
from utils.security import encrypt_text
from state import AppState

def add_diary_note_function(page : ft.Page) :
    '''Функция управляет интерфейсом добавления записи в дневник'''
    page.title = "Silo-Core Меню добавления записи в дневник"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.clean()
    page.window_width = 1920
    page.window_height = 1080
    page.theme_mode = ft.ThemeMode.DARK

    diary_note = ft.TextField(label="Ваша запись в дневник",multiline=True,min_lines=3,max_lines=8)
    
    confirm_add = ft.FilledButton(content=ft.Text("Сохранить данные"),disabled=True)

    btn_back = ft.FilledButton(content=ft.Text("Назад в меню"))

    def go_back(e):
        from view.diary.diary_interface import diary_data_operation
        diary_data_operation(page)
        page.update()

    def valiable_name(e) :
        if diary_note.value.strip() :
            confirm_add.disabled = False
        else :
            confirm_add.disabled = True
        page.update()

    def add_data_to_diary(e) :
        from db_manager.work_with_personal_diary import add_data_to_diary
        master_password = AppState.master_password
        diary_note_raw = encrypt_text(diary_note.value,master_password)
        add_diary_note = add_data_to_diary(diary_note_raw)
        if add_diary_note == "success" :
            page.add(ft.Text("Данные успешно записаны",color=ft.Colors.GREEN_ACCENT))

            diary_note.value = ""
            
            confirm_add.disabled = True
            page.update()

    diary_note.on_change = valiable_name
    confirm_add.on_click = add_data_to_diary
    btn_back.on_click = go_back
        
    page.add(
        ft.Column([
            diary_note,
            confirm_add,
            btn_back
        ])
    )
    page.update()
