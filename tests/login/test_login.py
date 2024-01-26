import logging
import os

import pytest
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Pytest_Logger")


@pytest.fixture
def ajax_email():
    return os.getenv("AJAX_EMAIL")


@pytest.fixture
def ajax_password():
    return os.getenv("AJAX_PASSWORD")


def get_credentials(request, email, password):
    if email in ["ajax_email"]:
        email = request.getfixturevalue(email)
    if password in ["ajax_password"]:
        password = request.getfixturevalue(password)
    return email, password


@pytest.mark.parametrize(
    argnames="email, password, expected",
    argvalues=[
        ("", "", False),
        ("SomeTingWong@gmail.com", "ajax_password", False),
        ("ajax_email", "InvalidPassword", False),
        ("ajax_email", "ajax_password", True),
    ],
    ids=[
        "Both email and password are empty",
        "Email is incorrect, password is correct",
        "Email is correct, password is incorrect",
        "All credentials are correct",
    ],
)
def test_user_login_data(user_login_fixture, email: str, password: str, expected: bool, request) -> None:
    logging.info("Starting test...")
    login_page = user_login_fixture

    email, password = get_credentials(request, email, password)

    login_page.log_in(email, password)
    assert login_page.check_if_logged_in() == expected

    login_page.driver.reset()
    logging.info("Test passed successfully")
