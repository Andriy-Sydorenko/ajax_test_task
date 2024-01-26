import logging
import os

from dotenv import load_dotenv

from framework.locators import *

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Pytest_Logger")


def get_sidebar_elements():
    return [APP_SETTINGS, APP_HELP, APP_LOGS, APP_CAMERA, APP_ADD_HUB, APP_TERMS_OF_USE]


def test_sidebar_elements_displayed(user_login_fixture):
    logging.info("Starting test for sidebar elements")

    email = os.getenv("AJAX_EMAIL")
    password = os.getenv("AJAX_PASSWORD")
    page = user_login_fixture
    page.log_in(email, password)
    sidebar_button = page.wait_for_ui_element(SIDE_BAR_BUTTON)
    page.click_element(sidebar_button)

    sidebar_elements = get_sidebar_elements()
    for elem_locator in sidebar_elements:
        sidebar_element = page.find_element_by_locator(elem_locator)
        assert sidebar_element.is_displayed()
        assert sidebar_element.is_enabled()

    logging.info("Sidebar elements test completed successfully")
