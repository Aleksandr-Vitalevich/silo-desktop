import flet as ft
from db_manager.work_with_personal_safe import add_data
from utils.security import encrypt_text
from state import AppState
from utils.page_config import configure_base_page

def add_data_function(page : ft.Page) :
    '''Функция управляет интерфейсом добавления данных в мои пароли и сервисы'''
    configure_base_page(page,"Silo-Core Меню добавления записей в сервис")

    name_service = ft.TextField(label = "Введите название сервиса")
    login_service = ft.TextField(label = "Введите логин")
    password_service = ft.TextField(label = "Введите пароль",password=True,can_reveal_password=True)
    site_service = ft.TextField(label= "Ссылка")
    token_service = ft.TextField(label= "Токен")
    other_need_information_service = ft.TextField(label="Дополнительная информация",multiline=True,min_lines=3,max_lines=8)
    
    confirm_add = ft.FilledButton(content=ft.Text("Сохранить данные"),disabled=True)

    btn_back = ft.FilledButton(content=ft.Text("Назад в меню"))

    def go_back(e):
        from view.safe.safe_interface import add_data_operation
        add_data_operation(page)
        page.update()

    def valiable_name(e) :
        if name_service.value.strip() :
            confirm_add.disabled = False
        else :
            confirm_add.disabled = True
        page.update()

    def add_data_to_safe(e) :
        master_password = AppState.master_password
        dct_add = {
                "name_service" : name_service.value,
                "login_service" : login_service.value,
                "password_service" : encrypt_text(password_service.value,master_password),
                "site_service" : encrypt_text(site_service.value,master_password),
                "token_service" : encrypt_text(token_service.value,master_password),
                "other_need_information_service" : encrypt_text(other_need_information_service.value,master_password)
                }
        add_personal_data = add_data(dct_add)
        if add_personal_data == "success" :
            page.add(ft.Text("Данные успешно записаны",color=ft.Colors.GREEN_ACCENT))

            name_service.value = ""
            login_service.value = ""
            password_service.value = ""
            site_service.value = ""
            token_service.value = ""
            other_need_information_service.value = ""
            
            confirm_add.disabled = True
            page.update()

    name_service.on_change = valiable_name
    confirm_add.on_click = add_data_to_safe
    btn_back.on_click = go_back
        
    page.add(
        ft.Column([
            name_service,
            login_service,
            password_service,
            site_service,
            token_service,
            other_need_information_service,
            confirm_add,
            btn_back
        ])
    )
    page.update()
