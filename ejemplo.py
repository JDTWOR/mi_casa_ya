import flet as ft

def main(page: ft.Page):
    texto = ft.Text("hernan es gay")

    page.add(texto)

ft.app(target=main, view=ft.WEB_BROWSER)
