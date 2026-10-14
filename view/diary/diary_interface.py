import flet as ft
from utils.page_config import configure_base_page


def diary_data_operation(page : ft.Page) :
    '''Основная функция модуля дневник'''
    configure_base_page(page,"Silo-Core Меню управления Дневником")

    add_data = ft.FilledButton(content=ft.Text("Добавить запись"))
    show_data_btn = ft.FilledButton(content=ft.Text("Показать записи"))

    btn_back = ft.FilledButton(content=ft.Text("Назад в меню"))
    
    def go_back(e):
        from view.main_interface import main_interface_operation
        main_interface_operation(page)
        page.update()

    def go_to_add_data_function(e) :
        from view.diary.add_diary_note_interface import add_diary_note_function
        add_diary_note_function(page)
        page.update()

    def go_to_show_data_function(e) :
        from view.diary.show_diary_note_interface import show_diary_note_function
        show_diary_note_function(page)
        page.update()

    
    
    add_data.on_click = go_to_add_data_function
    show_data_btn.on_click = go_to_show_data_function
    btn_back.on_click = go_back

    
    page.add(
        ft.Column([
            add_data,
            show_data_btn,
            btn_back
        ])
    )
    page.update()
