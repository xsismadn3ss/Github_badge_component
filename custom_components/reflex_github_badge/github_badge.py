"""Reflex custom component GithubBadge."""

import reflex as rx
import requests


class GithubBadge(rx.Component):
    """#### Github Badge Component
    args:
    * **username**: enter your github username
    * **description**: set a description to show
    """

    # The React library to wrap.
    library = "Fill-Me"

    # The React component tag.
    tag = "Fill-Me"

    @classmethod
    def __get_user_data__(cls, username) -> dict:
        user_data = {
            "username": "",
            "name": "",
            "html_url": "",
            "avatar_url": "",
            "location": "unknown",
            "public_repos": "0",
            "followers": "0",
        }
        data = requests.get(f"https://api.github.com/users/{username}").json()

        if "html_url" in data:
            user_data["username"] = username
            user_data["name"] = user_data["name"]
            user_data["html_url"] = data["html_url"]
            user_data["avatar_url"] = data["avatar_url"]
            user_data["location"] = (
                data["location"] if data["location"] != None else "unknown"
            )
            user_data["public_repos"] = data["public_repos"]
            user_data["followers"] = data["followers"]

        else:
            user_data["html_url"] = f"https://github.com/{username}"
            user_data["name"] = username
            user_data["username"] = username

        return user_data

    @classmethod
    def __render_data__(cls, data: dict, description: str):
        items = rx.flex(
            rx.text(
                rx.cond(data["name"] == "", data["username"], data["name"]),
                size="4",
                weight="bold",
            ),
            rx.flex(
                rx.link(
                    rx.text("@" + data["username"], size="2", weight="bold"),
                    href=data["html_url"],
                ),
                rx.flex(
                    rx.icon("map-pin", size=15, color="gray"),
                    rx.text(
                        data["location"], weight="bold", size="2", color_scheme="gray"
                    ),
                ),
                justify="between",
                spacing="2",
            ),
            rx.hstack(
                rx.flex(
                    rx.text("followers:", weight="bold", size="1", color_scheme="gray"),
                    rx.text(data["followers"], weight="light", size="1"),
                    spacing="1",
                ),
                rx.flex(
                    rx.text(
                        "repositories:", weight="bold", size="1", color_scheme="gray"
                    ),
                    rx.text(data["public_repos"], weight="light", size="1"),
                    spacing="2",
                ),
                justify="between",
                width="100%",
            ),
            rx.text(description, weight="regular"),
            direction="column",
            spacing="1",
        )

        return items

    @classmethod
    def __render_picture__(cls, src: str, username: str):
        if src != "":
            avatar = rx.avatar(src=src, radius="full", size='7')
        else:
            avatar = rx.avatar(
                fallback=f"{username[0:2]}".upper(),
                radius="full",
                size='7'
            )
        return avatar

    @classmethod
    def create(cls, username: str = "github", description: str = "Hello world 👋"):
        dark, light = "#404040", "d1d1d1"
        data = cls.__get_user_data__(username=username)
        items = cls.__render_data__(data=data, description=description)
        avatar = cls.__render_picture__(src=data["avatar_url"], username=username)

        return (
            rx.desktop_only(
                rx.card(
                    rx.flex(
                        rx.vstack(
                            avatar,
                            justify='center',
                            align='center'
                        ),
                        items,
                        direction="row",
                        spacing='3'
                    ),
                    size='2'
                )
            ),
            rx.mobile_and_tablet(
                rx.card(
                    rx.flex(
                        rx.vstack(
                            avatar,
                            justify='center',
                            align='center'
                        ),
                        items,
                        direction="column",
                        spacing='3'
                    ),
                    size='1'
                )
            ),
        )


github_badge = GithubBadge.create
