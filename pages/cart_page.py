from appium.webdriver.common.appiumby import AppiumBy
from utils.element_util import ElementUtil
import logging
import time

from utils.gestures_util import GesturesUtil

# Set up logging configuration
logging.basicConfig(level=logging.INFO)


class SauceDemoCartPage(ElementUtil):
    def __init__(self, driver):
        super().__init__(driver)
        # Initialize GesturesUtil
        self.gesture_util = GesturesUtil(driver)
        # Element locator
        self.checkout_button = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT")
        # self.product_pod = (AppiumBy.XPATH, "//android.widget.TextView[@text='Sauce Labs Backpack']")
        self.product_pod = (AppiumBy.XPATH, "//android.widget.TextView[@text='Sauce Labs Backpack']")
        self.delete_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='󰩺']")

    def click_on_checkout_button(self):
        self.wait_for_element(*self.checkout_button)
        self.click_on_element(self.checkout_button)

    def swipe_to_remove(self):
        self.wait_for_element(*self.product_pod)
        self.gesture_util.swipe_item_left(self.product_pod)
        self.wait_for_element(*self.delete_button)
        self.click_on_element(self.delete_button)
        self.wait_for_invisibility_of_element(*self.product_pod)


