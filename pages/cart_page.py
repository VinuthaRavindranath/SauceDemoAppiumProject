from appium.webdriver.common.appiumby import AppiumBy
from utils.element_util import ElementUtil
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)


class SauceDemoCartPage(ElementUtil):
    def __init__(self, driver):
        super().__init__(driver)
        # Element locator
        self.checkout_button = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT")

    def click_on_checkout_button(self):
        self.wait_for_element(*self.checkout_button)
        self.driver.find_element(*self.checkout_button).click()
