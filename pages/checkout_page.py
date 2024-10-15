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

    def enter_first_name(self, firstname):
        self.wait_for_element(*self.first_name)
        self.send_keys_to_element(self.first_name, firstname)

    def enter_last_name(self, lastname):
        self.send_keys_to_element(self.last_name, lastname)

    def enter_postal_code(self, postalcode):
        self.send_keys_to_element(self.postal_code, postalcode)

    def click_on_continue_button(self):
        self.click_on_element(self.continue_button)

    def click_on_finish_button(self):
        resource_id_to_scroll_to = "test-FINISH"
        element = self.scroll_to_element(resource_id_to_scroll_to)
        element.click()
