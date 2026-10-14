import flet as ft
from db_manager.work_with_add_user import add_user
from view.main_interface import main_interface_operation
from state import AppState
from utils.page_config import configure_base_page

def registration_function(page : ft.Page) :
    '''Функция регистрации в приложении'''
    configure_base_page(page,"Silo-Core Меню регистрации")

    user_login = ft.TextField(label = "Введите логин")
    user_password = ft.TextField(label = "Введите пароль",password=True,can_reveal_password=True)

    confirm_registration = ft.FilledButton(content=ft.Text("Регситрация"),disabled=True)

    def valiable_inputs(e) :
        '''Проверка заполнения полей ввода'''
        if user_login.value.strip() and user_password.value.strip() :
            confirm_registration.disabled = False
        else :
            confirm_registration.disabled = True
        page.update()
    
    def on_registration_click(e) :
        '''Функция вызывает базу данных'''
        registration = add_user(user_login.value.strip(),user_password.value.strip())
        if registration == "success" :
            AppState.master_password = user_password.value.strip()
            page.clean()
            main_interface_operation(page)
    user_login.on_change = valiable_inputs
    user_password.on_change = valiable_inputs
    confirm_registration.on_click = on_registration_click

    page.add(
        ft.Column([
            user_login,
            user_password,
            confirm_registration
        ])
    )
    page.update()
