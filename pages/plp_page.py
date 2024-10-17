import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import AppConstants
from utils.element_util import ElementUtil
import logging

from utils.gestures_util import GesturesUtil

# Set up logging configuration
logging.basicConfig(level=logging.INFO)


class SauceDemoPlpPage(ElementUtil):

    def __init__(self, driver):
        super().__init__(driver)
        # Initialize GesturesUtil
        self.gesture_util = GesturesUtil(driver)

        # Element locators
        self.first_product_on_plp = (
            AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='test-Item'])[1]/android.view.ViewGroup")
        self.add_to_cart = (AppiumBy.XPATH, "(//android.widget.TextView[@text='ADD TO CART'])")
        self.cart_icon = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Cart']")
        self.cart_count = (AppiumBy.XPATH, "//android.widget.TextView")
        self.add_to_cart_drag_zone = (AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='test-Drag Handle'])[2]")
        self.add_to_cart_drop_zone = (AppiumBy.ACCESSIBILITY_ID, "test-Cart drop zone")
        self.burger_menu = (AppiumBy.XPATH,
                            "//android.view.ViewGroup[@content-desc='test-Menu']/android.view.ViewGroup/android.widget.ImageView")
        self.logout_button = (AppiumBy.ACCESSIBILITY_ID, "test-LOGOUT")
        self.first_product= (AppiumBy.XPATH,"//android.widget.TextView[@content-desc='test-Item title' and @text='Sauce Labs Backpack']")


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
        # self.wait_for_element(*self.add_to_cart)
        self.click_on_element(self.add_to_cart)
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
        count = self.get_text_of_element(self.cart_count)
        logging.info(f"Current cart count: {count}")
        return count

    def click_on_mini_cart(self):
        self.click_on_element(self.cart_icon)

    def add_product_by_dragging_to_cart(self):
        self.wait_for_element(*self.add_to_cart_drag_zone)
        # Use the gestures_util instance to perform the drag and drop
        self.gesture_util.drag_and_drop(self.add_to_cart_drag_zone, self.add_to_cart_drop_zone)

    def do_logout(self):
        self.click_on_element(self.burger_menu)
        self.wait_for_element(*self.logout_button)
        self.click_on_element(self.logout_button)

    def add_multiple_products_to_cart(self):
        self.click_on_element(self.add_to_cart)
        resource_id_to_scroll="Sauce Labs Bolt T-Shirt"
        self.scroll_to_element(resource_id_to_scroll,"text")
        self.click_on_element(self.add_to_cart)

    def click_on_first_product(self):
        self.wait_for_element(*self.first_product)
        self.click_on_element(self.first_product)
