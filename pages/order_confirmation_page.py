from appium.webdriver.common.appiumby import AppiumBy
from utils.element_util import ElementUtil
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)


class SauceDemoOrderConfirmationPage(ElementUtil):
    def __init__(self, driver):
        super().__init__(driver)
        # Element locator
        self.checkout_complete_header = (AppiumBy.XPATH, "//android.widget.TextView[@text='CHECKOUT: COMPLETE!']")

    def validate_presence_of_checkout_complete(self):
        """
        Validate that the first product on the product listing page is present.

        This method waits for the first product element to be present on the page.

        Returns:
            None: This method does not return a value.
        """
        logging.info("Validating presence of the first product.")
        self.wait_for_presence(*self.checkout_complete_header)