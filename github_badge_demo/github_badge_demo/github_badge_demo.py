"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx

from reflex_github_badge import github_badge

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.center(
        rx.color_mode.button(position='top-right'),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="5"),
            rx.text(
                "Test your custom component by editing ", 
                rx.code(filename),
                font_size="2em",
            ),
            github_badge(),
            align="center",
            spacing="7",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
