import flet as ft

class App:

    # Init function
    def __init__(self, page: ft.Page) -> None:
        # Make a class global variable called pg from page local variable
        self.pg = page

        # Config page
        self.config()

        # Create widgets


        # Add widgets

        widgets = []
        self.add_widgets(widgets)

    # Page functions
    def config(self) -> None:
        self.pg.title = "Mi App"
        self.pg.bgcolor = ft.colors.BLUE_GREY_900
        self.pg.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def add_widgets(self, widgets: list) -> None:
        for widget in widgets:
            self.pg.add(widget)

    # Button functions


def main(page: ft.Page):
    app = App(page)

if __name__ == '__main__':
    ft.app(target=main)