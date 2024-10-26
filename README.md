# github-badge

A Reflex custom component github-badge.

![github_badge](image.png)

## Installation

```bash
pip install reflex-github-badge
```

## Import

```python
from reflex_github_badge.github_adge import github_badge
```

## Usage example

```python
def GithubCard() -> rx.Component:
    return github_badge(
        username="(your username)", 
        description="Hello world 👋"
    )
```
