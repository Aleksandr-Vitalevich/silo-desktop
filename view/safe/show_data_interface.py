import flet as ft
from state import AppState
from utils.page_config import configure_base_page

def show_data_function(page : ft.Page) :
    '''Функция управляет интерфейсом отображения данных в мои пароли и сервисы'''
    configure_base_page(page,"Silo-Core Меню отображения данных")

    master_password = AppState.master_password
    table_container = ft.Container()

    btn_back = ft.FilledButton(content=ft.Text("Назад в меню"))

    
    from utils.security import decrypt_text
    from db_manager.work_with_personal_safe import show_data
    data = show_data()
    table_rows = []
    for row in data :
        id_service = row[0]
        name_service_decript = row[1]
        login_service_decript = row[2]
        password_service_decript = decrypt_text(row[3],master_password)
        site_service_decript = decrypt_text(row[4],master_password)
        token_service_decript = decrypt_text(row[5],master_password)
        other_need_information_service_decript = decrypt_text(row[6],master_password)

        table_rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(id_service,selectable=True,color=ft.Colors.BROWN_200)),
                    ft.DataCell(ft.Text(name_service_decript,selectable=True,color=ft.Colors.BROWN_200)),
                    ft.DataCell(ft.Text(login_service_decript,selectable=True,color=ft.Colors.BROWN_200)),
                    ft.DataCell(ft.Text(password_service_decript,selectable=True,color=ft.Colors.BROWN_200)),
                    ft.DataCell(ft.TextButton(
                        content=ft.Text(site_service_decript,
                        max_lines=3,
                        overflow=ft.TextOverflow.ELLIPSIS,color=ft.Colors.BROWN_200
                        ),url=site_service_decript if site_service_decript.startswith("http") else f"https://{site_service_decript}",
                        width=250 
                        )),
                    ft.DataCell(ft.Text(token_service_decript,
                        max_lines=3,
                        overflow=ft.TextOverflow.ELLIPSIS,expand=True,width=250,selectable=True,color=ft.Colors.BROWN_200 )),
                    ft.DataCell(ft.Text(
                        other_need_information_service_decript,
                        max_lines=3,
                        overflow=ft.TextOverflow.ELLIPSIS,expand=True,width=250,selectable=True,color=ft.Colors.BROWN_200)),
                ]
            )
        )

    passwords_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("id")),
            ft.DataColumn(ft.Text("Сервис")),
            ft.DataColumn(ft.Text("Логин")),
            ft.DataColumn(ft.Text("Пароль")),
            ft.DataColumn(ft.Text("Сайт")),
            ft.DataColumn(ft.Text("Токен")),
            ft.DataColumn(ft.Text("Дополнительная информация")),
        ],
        rows = table_rows
    )

    horizontal_scroll = ft.Row(
            controls=[passwords_table],
            scroll=ft.ScrollMode.ALWAYS,
            expand=True
        )

    table_container.content = ft.ListView(controls=[horizontal_scroll], expand=True, spacing=10)
    page.update()



    def go_back(e):
        from view.safe.safe_interface import add_data_operation
        add_data_operation(page)
        page.update()

    btn_back.on_click = go_back

    page.add(
        ft.Column([
            table_container,
            btn_back
        ],expand=True)
    )
    page.update()
