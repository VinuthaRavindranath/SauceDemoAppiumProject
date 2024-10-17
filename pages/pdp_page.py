import time

from appium.webdriver.common.appiumby import AppiumBy
from utils.element_util import ElementUtil
import logging

from utils.gestures_util import GesturesUtil

# Set up logging configuration
logging.basicConfig(level=logging.INFO)


class SauceDemoPdpPage(ElementUtil):

    def __init__(self, driver):
        super().__init__(driver)
        # Initialize GesturesUtil
        self.gesture_util = GesturesUtil(driver)

        # Element locators
        self.product_image = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Image Container']/android.widget.ImageView")

    # def zoom_product_image(self):
    #     self.wait_for_element(*self.product_image)
    #     self.gesture_util.pinch(self.product_image)
    #     time.sleep(3)