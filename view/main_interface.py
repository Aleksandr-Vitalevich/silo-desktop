import flet as ft
from state import AppState


def main_interface_operation(page : ft.Page) :
    '''Основная функция переключатель'''
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.clean()
    page.title = "Silo-Core Главное меню"
    page.window_width = 1920
    page.window_height = 1080
    page.theme_mode = ft.ThemeMode.DARK
    master_password = AppState.master_password

    def go_to_log_out(e) :
        from state import AppState
        from main import main_operation
        AppState.master_password = None
        main_operation(page)
        page.update()

    def got_to_add_data_operation(e) :
        from view.safe.safe_interface import add_data_operation
        add_data_operation(page)
        page.update()

    def go_to_diary_data_operation(e) :
        from view.diary.diary_interface import diary_data_operation
        diary_data_operation(page)
        page.update()

    user_data = ft.FilledButton(content=ft.Text("Мои пароли и сервисы"))
    user_diary = ft.FilledButton(content=ft.Text("Мой дневник"))
    user_files = ft.FilledButton(content=ft.Text("Мои файлы"))
    user_log_out = ft.FilledButton(content=ft.Text("Выход"))

    user_data.on_click = got_to_add_data_operation
    user_diary.on_click = go_to_diary_data_operation
    #user_files.on_click = 
    user_log_out.on_click = go_to_log_out



    page.add(
            ft.Column([
                user_data,
                user_diary,
                user_files,
                user_log_out
            ])
        )
    page.update()