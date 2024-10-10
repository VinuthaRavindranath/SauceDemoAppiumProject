from appium.webdriver.common.appiumby import AppiumBy
from utils.element_util import ElementUtil
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)


class SauceDemoPlpPage(ElementUtil):

    def __init__(self, driver):
        super().__init__(driver)
        # Element locators
        self.first_product_on_plp = (
            AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='test-Item'])[1]/android.view.ViewGroup")
        self.add_to_cart = (AppiumBy.XPATH, "(//android.widget.TextView[@text='ADD TO CART'])")
        self.cart_icon = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Cart']")
        self.cart_count = (AppiumBy.XPATH, "//android.widget.TextView")

    def validate_presence_of_first_product(self):
        """
        Validate that the first product on the product listing page is present.

        This method waits for the first product element to be present on the page.

        Returns:
            None: This method does not return a value.
        """
        logging.info("Validating presence of the first product.")
        self.wait_for_presence(*self.first_product_on_plp)

    def add_product_to_cart(self):
        """
        Add the first product to the shopping cart.

        This method waits for the "ADD TO CART" button to be present and then clicks it.

        Returns:
            None: This method does not return a value.
        """
        logging.info("Adding product to cart.")
        self.wait_for_element(*self.add_to_cart)
        self.driver.find_element(*self.add_to_cart).click()
        logging.info("Product added to cart.")

    def get_cart_count(self):
        """
        Get the current count of items in the shopping cart.

        This method waits for the cart count element to be present and retrieves its text.

        Returns:
            str: The text content of the cart count element.
        """
        logging.info("Retrieving cart count.")
        self.wait_for_element(*self.cart_count)
        count = self.driver.find_element(*self.cart_count).text
        logging.info(f"Current cart count: {count}")
        return count

    def click_on_mini_cart(self):
        self.driver.find_element(*self.cart_icon).click()
