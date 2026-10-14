import flet as ft

def configure_base_page(page: ft.Page, title_text: str):
    """
    Глобальный конфигуратор окон Silo-Core.
    Устанавливает тему, центрирование, размеры и адаптивное поведение.
    """
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.clean()
    page.title = f"Silo-Core | {title_text}"
    page.theme_mode = ft.ThemeMode.DARK
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.window_width = 1280
    page.window_height = 800
    page.window_min_width = 800  
    page.window_min_height = 600

    def on_window_resize(e):
        page.update()

    page.on_window_resized = on_window_resize
    page.clean()
