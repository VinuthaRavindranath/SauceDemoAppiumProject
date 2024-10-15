from appium.webdriver.common.appiumby import AppiumBy
from utils.element_util import ElementUtil
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)


class SauceDemoPdpPage(ElementUtil):

    def __init__(self, driver):
        super().__init__(driver)
        # Element locators
        self.first_product_on_plp = (AppiumBy.XPATH, "")