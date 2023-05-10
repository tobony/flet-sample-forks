import flet
from flet import Page, Text


def main(page: Page):
    page.title = "Anasayfa"

    t = Text(value="Hello, world!")
    page.controls.append(t)
    page.update()


# flet.app(target=main)
flet.app(target=main, port=8080, view=flet.WEB_BROWSER)
