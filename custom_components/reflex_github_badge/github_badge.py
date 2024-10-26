"""Reflex custom component GithubBadge."""
import reflex as rx
import requests


class GithubBadge(rx.Component):
    """Github Badge Component
    args:
    * username: enter your github username
    * description: set a description to show
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
            "location": "",
            "bio": "",
            "public_repos": "",
            "followers": "",
        }
        data = requests.get(f"https://api.github.com/users/{username}").json()

        if "html_url" in data:
            user_data["username"] = username
            user_data["name"] = (
                user_data["name"] if user_data["name"] != "" else username
            )
            user_data["html_url"] = data["html_url"]
            user_data["avatar_url"] = data["avatar_url"]
            user_data["location"] = (
                data["location"] if user_data["location"] != "" else ""
            )
            user_data["bio"] = (
                data["bio"] if user_data["bio"] != "" else "..."
            )
            user_data["public_repos"] = data["public_repos"]
            user_data["followers"] = data["followers"]
            print(user_data)

        else:
            user_data["html_url"] = f"https://github.com/{username}"

        return user_data

    @classmethod
    def __render_data__(cls, data: dict, description: str):
        if (
            data["name"],
            data["location"],
            data["bio"],
            data["public_repos"],
            data["followers"],
        ) == "":
            print("Github has blocked the request or your profile does not exist ⚠️")
            items = rx.flex(
                rx.text(data["username"], size="4", weight="bold"),
                rx.text(description, weight="regular"),
                spacing="1",
                direction="column",
            )

        else:
            print("data succesfully obtained ✅")
            items = rx.flex(
                rx.text(
                    data["name"],
                    size="4",
                    weight="bold",
                ),
                rx.text(f"@{data['username']}", size="1", weight="regular"),
                rx.hstack(
                    rx.flex(
                        rx.text("followers:", weight="bold", size="1"),
                        rx.text(data["followers"], weight="light", size="1"),
                        spacing="1",
                    ),
                    rx.flex(
                        rx.text("repositories:", weight="bold", size="1"),
                        rx.text(data["public_repos"], weight="light", size="1"),
                        spacing="2",
                    ),
                    rx.text(data["location"], weight="bold", size="1"),
                    justify="between",
                    widht="100%",
                ),
                rx.flex(
                    rx.text("bio:", weight="bold", size="2"),
                    rx.text(data["bio"], weight="light", size="2"),
                    spacing="2",
                ),
                rx.text(description, weight="regular"),
                direction="column",
                spacing="1",
            )

        return items

    @classmethod
    def __render_picture__(cls, src: str, username: str):
        if src != "":
            avatar = rx.avatar(src=src, radius="full", size="8", margin_bottom="0.5rem")
        else:
            avatar = rx.avatar(
                fallback=f"{username[0:2]}".upper(),
                radius="full",
                size="8",
                margin_bottom="0.5rem",
            )
        return avatar

    @classmethod
    def create(cls, username: str = "github", description: str = ""):
        dark, light = "#404040", "d1d1d1"
        data = cls.__get_user_data__(username=username)
        items = cls.__render_data__(data=data, description=description)
        avatar = cls.__render_picture__(src=data["avatar_url"], username=username)

        return rx.card(
            rx.link(
                rx.flex(
                    rx.vstack(avatar, align="center", justify="center"),
                    items,
                    spacing="4",
                    color=rx.color_mode_cond(dark, light),
                ),
                href=data["html_url"],
            ),
            size="2",
        )


github_badge = GithubBadge.create
