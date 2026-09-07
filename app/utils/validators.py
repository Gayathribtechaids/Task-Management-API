import re


def validate_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(pattern, email) is not None


def validate_task_title(title: str) -> bool:
    return len(title.strip()) > 0

def validate_task_status(status: str) -> bool:
    allowed_status = ["pending", "in_progress", "completed"]

    return status in allowed_status