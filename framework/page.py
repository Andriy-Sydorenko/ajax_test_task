from appium.webdriver.common.appiumby import AppiumBy


class Page:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self):
        raise NotImplementedError

    def find_element_by_locator(self, locator_data: tuple[AppiumBy, str]):
        return self.driver.find_element(*locator_data)
