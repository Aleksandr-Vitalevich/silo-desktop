import flet as ft
from state import AppState
from utils.page_config import configure_base_page


def main_interface_operation(page : ft.Page) :
    '''Основная функция переключатель'''
    configure_base_page(page,"Silo-Core Главное меню")

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
    user_log_out = ft.FilledButton(content=ft.Text("Выход"))

    user_data.on_click = got_to_add_data_operation
    user_diary.on_click = go_to_diary_data_operation
    user_log_out.on_click = go_to_log_out



    page.add(
            ft.Column([
                user_data,
                user_diary,
                user_log_out
            ])
        )
    page.update()