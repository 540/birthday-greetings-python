from typing import TypedDict


class Mail(TypedDict):
    sender: str
    recipient: str
    subject: str
    body: str
