import time

from appium.webdriver.common.appiumby import AppiumBy
from utils.element_util import ElementUtil
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)


class SauceDemoCheckoutPage(ElementUtil):
    def __init__(self, driver):
        super().__init__(driver)
        # Element locator
        self.first_name = (AppiumBy.ACCESSIBILITY_ID, "test-First Name")
        self.last_name = (AppiumBy.ACCESSIBILITY_ID, "test-Last Name")
        self.postal_code = (AppiumBy.ACCESSIBILITY_ID, "test-Zip/Postal Code")
        self.continue_button = (AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE")
        self.finish_button = (AppiumBy.ACCESSIBILITY_ID, "test-FINISH")

    def enter_first_name(self):
        self.wait_for_element(*self.first_name)
        self.driver.find_element(*self.first_name).send_keys("automation")

    def enter_last_name(self):
        self.driver.find_element(*self.last_name).send_keys("user")

    def enter_postal_code(self):
        self.driver.find_element(*self.postal_code).send_keys("12345")

    def click_on_continue_button(self):
        self.driver.find_element(*self.continue_button).click()

    def click_on_finish_button(self):
        resource_id_to_scroll_to = "test-FINISH"
        element = self.scroll_to_element(resource_id_to_scroll_to)
        element.click()
