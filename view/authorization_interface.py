import flet as ft
from db_manager.work_with_add_user import check_user_authorization
from view.main_interface import main_interface_operation
from state import AppState
from utils.page_config import configure_base_page

def authorization_function(page : ft.Page) :
    '''Функция регистрации в приложении'''
    configure_base_page(page,"Silo-Core Меню авторизации")

    user_login = ft.TextField(label = "Введите логин")
    user_password = ft.TextField(label = "Введите пароль",password=True,can_reveal_password=True)
    confirm_authorization = ft.FilledButton(content=ft.Text("Авторизация"),disabled=True)

    def valiable_inputs(e) :
        '''Проверка заполнения полей ввода'''
        if user_login.value.strip() and user_password.value.strip() :
            confirm_authorization.disabled = False
        else :
            confirm_authorization.disabled = True
        page.update()
        
    def on_authorization_click(e) :
        '''Функция вызывает базу данных'''
        authorization = check_user_authorization(user_login.value.strip(),user_password.value.strip())
        if authorization :
            AppState.master_password = user_password.value.strip()
            page.clean()
            main_interface_operation(page)
        else :
            page.add(ft.Text("Добро пожаловать",color=ft.Colors.RED_ACCENT))
            
    
    user_login.on_change = valiable_inputs
    user_password.on_change = valiable_inputs
    confirm_authorization.on_click = on_authorization_click
    
    page.add(
        ft.Column([
            user_login,
            user_password,
            confirm_authorization
        ])
    )
    page.update()
