from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_ui_element(self, locator_data: tuple[AppiumBy, str]):
        return WebDriverWait(self.driver, timeout=10).until(
            ec.presence_of_element_located(locator=locator_data)
        )

    @staticmethod
    def click_element(web_element: WebElement) -> None:
        web_element.click()

    @staticmethod
    def input_data(web_element: WebElement, data: str) -> None:
        web_element.send_keys(data)

    def find_element_by_locator(self, locator_data: tuple[AppiumBy, str]) -> WebElement:
        return self.driver.find_element(*locator_data)
