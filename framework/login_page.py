from appium.webdriver.common.appiumby import AppiumBy

from .page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from appium.webdriver.webelement import WebElement


class LoginPage(Page):
    def log_in(self, email: str, password: str) -> None:

        pass  # TODO: implement this logic

    def wait_for_next_step(self, locator_data: tuple[AppiumBy, str]) -> WebElement:
        return WebDriverWait(self.driver, timeout=30).until(
            ec.presence_of_element_located(locator=locator_data))

    def check_if_logged_in(self) -> bool:
        try:
            self.wait_for_next_step((AppiumBy.ID, "com.ajaxsystems:id/hubAdd"))
            return True
        except (NoSuchElementException, TimeoutException):
            return False
