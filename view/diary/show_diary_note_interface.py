import flet as ft
from state import AppState

def show_diary_note_function(page : ft.Page) :
    '''Функция управляет интерфейсом отображения данных в дневнике'''
    page.title = "Silo-Core Меню отображения данных"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.clean()
    page.window_width = 1920
    page.window_height = 1080
    page.theme_mode = ft.ThemeMode.DARK

    master_password = AppState.master_password
    table_rows = []

    btn_back = ft.FilledButton(content=ft.Text("Назад в меню"))

    
    from utils.security import decrypt_text
    from db_manager.work_with_personal_diary import show_data_to_diary

    try :
        diary_data = show_data_to_diary()
        for row in diary_data :
            try :
                decrypted_note = decrypt_text(row[1],master_password)
            except Exception:
                decrypted_note = row[1]
            data_create = row[2]
            table_rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(data_create,color=ft.Colors.BROWN_200)),
                        ft.DataCell(
                            ft.Text(
                                value=decrypted_note,
                                selectable=True,
                                max_lines=4,
                                overflow=ft.TextOverflow.ELLIPSIS,
                                color=ft.Colors.BROWN_200
                            )
                        ),
                    ]
                )
            )
        diary_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Дата и время")),
                ft.DataColumn(ft.Text("Мои записи")),
            ],
            rows=table_rows
        )
        content_view = ft.ListView(controls=[diary_table],expand=True,spacing=10)
    except Exception as e:
        content_view = ft.Text(f"Записей пока нет или база пуста", color="red")


    def go_back(e):
        from view.diary.diary_interface import diary_data_operation
        diary_data_operation(page)
        page.update()

    btn_back.on_click = go_back

    page.add(
        ft.Column([
            content_view,
            btn_back
        ],expand=True)
    )
    page.update()
