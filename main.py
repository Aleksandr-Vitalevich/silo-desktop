import flet as ft
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from view.authorization_interface import authorization_function
from view.registration_interface import registration_function
from db_manager.work_with_add_user import check_user_in_db

def main_operation(page : ft.Page) :
    '''Главная функция'''
    page.clean()
    if check_user_in_db() :
        authorization_function(page)
    else :
        registration_function(page)

    page.update()

if __name__ == "__main__":
    ft.run(main_operation)


