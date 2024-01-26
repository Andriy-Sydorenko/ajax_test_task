from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from framework import locators
from framework.page import Page

load_dotenv()


class LoginPage(Page):
    def log_in(self, email: str, password: str) -> None:
        go_to_login_button = self.find_element_by_locator(locators.GO_TO_LOGIN_BUTTON)
        self.click_element(go_to_login_button)

        email_field = self.wait_for_ui_element(locators.EMAIL_FIELD)
        password_field = self.find_element_by_locator(locators.PASSWORD_FIELD)

        self.input_data(email_field, email)
        self.input_data(password_field, password)

        submit_login_button = self.find_element_by_locator(locators.SUBMIT_LOGIN_BUTTON)
        self.click_element(submit_login_button)

    def check_if_logged_in(self) -> bool:
        try:
            self.wait_for_ui_element(locators.SIDE_BAR_BUTTON)
            return True
        except (NoSuchElementException, TimeoutException):
            return False
