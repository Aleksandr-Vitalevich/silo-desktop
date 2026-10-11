import flet as ft

def delete_files_function(page : ft.Page) :
    '''Функция управляет интерфейсом удаления файлов'''
    page.title = "Silo-Core Меню удаления записей в сервисе"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.clean()
    page.window_width = 1920
    page.window_height = 1080
    page.theme_mode = ft.ThemeMode.DARK

    id_service = ft.TextField(label = "Введите id сервиса")
    
    confirm_delete = ft.FilledButton(content=ft.Text("Удалить файл"),disabled=True)

    btn_back = ft.FilledButton(content=ft.Text("Назад в меню"))

    def valiable_name(e) :
        if id_service.value.strip() :
            confirm_delete.disabled = False
        else :
            confirm_delete.disabled = True
        page.update()
    
    def go_back(e):
        from view.files.files_interface import add_files_operation
        add_files_operation(page)
        page.update()

    def go_delete(e):
        from db_manager.work_with_personal_files import delete_file
        id_to_delete = int(id_service.value.strip())
        delete = delete_file(id_to_delete)
        if delete == "success" :
            page.add(ft.Text("Файл успешно удален",color=ft.Colors.GREEN_ACCENT))
            id_service.value = ''
            confirm_delete.disabled = True
            page.update()
        elif delete == "not find" :
            page.add(ft.Text("Файл не найден",color=ft.Colors.RED_ACCENT))
            id_service.value = ''
            confirm_delete.disabled = True
            page.update()
    
    id_service.on_change = valiable_name
    btn_back.on_click = go_back
    confirm_delete.on_click = go_delete
        
    page.add(
        ft.Column([
            id_service,
            confirm_delete,
            btn_back
        ])
    )
    page.update()
