import flet as ft


def add_data_operation(page : ft.Page) :
    '''Основная функция модуля данных'''
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.clean()
    page.title = "Silo-Core Меню управления Мои пароли и сервисы"
    page.window_width = 1920
    page.window_height = 1080
    page.theme_mode = ft.ThemeMode.DARK

    add_data = ft.FilledButton(content=ft.Text("Добавить сервис"))
    show_data_btn = ft.FilledButton(content=ft.Text("Показать данные"))
    delete_data_btn = ft.FilledButton(content=ft.Text("Удалить данные"))

    btn_back = ft.FilledButton(content=ft.Text("Назад в меню"))
    
    def go_back(e):
        from view.main_interface import main_interface_operation
        main_interface_operation(page)
        page.update()

    def go_to_add_data_function(e) :
        from view.safe.add_data_interface import add_data_function
        add_data_function(page)
        page.update()

    def go_to_show_data_function(e) :
        from view.safe.show_data_interface import show_data_function
        show_data_function(page)
        page.update()

    def go_to_delete_data_function(e) :
        from view.safe.delete_data_interface import delete_data_function
        delete_data_function(page)
        page.update()
    
    
    add_data.on_click = go_to_add_data_function
    show_data_btn.on_click = go_to_show_data_function
    delete_data_btn.on_click = go_to_delete_data_function
    btn_back.on_click = go_back

    
    page.add(
        ft.Column([
            add_data,
            show_data_btn,
            delete_data_btn,
            btn_back
        ])
    )
    page.update()
