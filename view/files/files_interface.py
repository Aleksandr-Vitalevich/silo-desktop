import flet as ft


def add_files_operation(page : ft.Page) :
    '''Основная функция модуля добавления файлов'''
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.clean()
    page.title = "Silo-Core Меню управления Мои файлы"
    page.window_width = 1920
    page.window_height = 1080
    page.theme_mode = ft.ThemeMode.DARK

    add_file = ft.FilledButton(content=ft.Text("Добавить файл"))
    show_file_btn = ft.FilledButton(content=ft.Text("Показать файлы"))
    delete_file_btn = ft.FilledButton(content=ft.Text("Удалить файлы"))

    btn_back = ft.FilledButton(content=ft.Text("Назад в меню"))
    
    def go_back(e):
        from view.main_interface import main_interface_operation
        main_interface_operation(page)
        page.update()

    def go_to_add_file_function(e) :
        from view.files.add_files_interface import add_file_function
        add_file_function(page)
        page.update()

    #def go_to_show_data_function(e) :
    #    from view.safe.show_data_interface import show_data_function
    #    show_data_function(page)
    #    page.update()

    def go_to_delete_files_function(e) :
        from view.files.delete_files_interface import delete_files_function
        delete_files_function(page)
        page.update()
    
    
    add_file.on_click = go_to_add_file_function
    #show_data_btn.on_click = go_to_show_data_function
    delete_file_btn.on_click = go_to_delete_files_function
    btn_back.on_click = go_back

    
    page.add(
        ft.Column([
            add_file,
            show_file_btn,
            delete_file_btn,
            btn_back
        ])
    )
    page.update()
