import re

import requests

EMAIL_RE = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.-]+$")


def add(a: int, b: int) -> int:
    return a + b


def is_valid_email(email: str) -> bool:
    return bool(EMAIL_RE.match(email))


def fetch_status(url: str, timeout: int = 5) -> int:
    return requests.get(url, timeout=timeout).status_code
