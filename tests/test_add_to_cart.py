import pytest
from conftest import appium_driver, logger
from pages import (
    SauceDemoLoginPage,
    SauceDemoPlpPage, SauceDemoCartPage
)
from constants import AppConstants


class TestAddToCart:

    @pytest.fixture(autouse=True)
    def setup(self, appium_driver):
        """Setup method to initialize page objects before each test."""
        logger.info("Initializing page objects for the test.")
        self.login_page = SauceDemoLoginPage(appium_driver)
        self.plp_page = SauceDemoPlpPage(appium_driver)
        self.cart_page=SauceDemoCartPage(appium_driver)

    @pytest.mark.usefixtures("appium_driver", "log_on_failure")
    def test_add_to_cart(self):
        """Test the functionality of adding a product to the cart."""
        logger.info("Starting test: test_add_to_cart")

        # Perform login
        self.login_page.do_login(AppConstants.STANDARD_USER, AppConstants.STANDARD_PASSWORD)

        # Add product to the cart
        self.plp_page.add_product_to_cart()
        logger.info("Product added to cart.")

        # Get the cart count and assert it
        cart_count = self.plp_page.get_cart_count()
        logger.info(f"Retrieved cart count: {cart_count}")

        # Assert that the cart count is as expected
        assert cart_count == "1", f"Expected cart count to be '1', but got '{cart_count}'."
        logger.info("Test completed successfully. Product added to cart.")

    @pytest.mark.usefixtures("appium_driver", "log_on_failure")
    def test_drag_product_into_cart(self):
        logger.info("Starting test: test_drag_product_into_cart")

        # Perform login
        self.login_page.do_login(AppConstants.STANDARD_USER, AppConstants.STANDARD_PASSWORD)

        # Add product to the cart by dragging the product and dropping to cart
        self.plp_page.add_product_by_dragging_to_cart()
        # Get the cart count and assert it
        cart_count = self.plp_page.get_cart_count()
        logger.info(f"Retrieved cart count: {cart_count}")

        # Assert that the cart count is as expected
        assert cart_count == "1", f"Expected cart count to be '1', but got '{cart_count}'."
        logger.info("Test completed successfully. Product added to cart.")

    @pytest.mark.usefixtures("appium_driver", "log_on_failure")
    def test_swipe_to_remove_product_from_cart(self):
        logger.info("Starting test: test_drag_product_into_cart")

        # Perform login
        self.login_page.do_login(AppConstants.STANDARD_USER, AppConstants.STANDARD_PASSWORD)

        # Add multiple products to the cart
        self.plp_page.add_multiple_products_to_cart()
        self.plp_page.click_on_mini_cart()
        self.cart_page.swipe_to_remove()
        cart_count = self.plp_page.get_cart_count()
        assert cart_count == "1", f"Expected cart count to be '1', but got '{cart_count}'."
        logger.info("Test completed successfully. Product deleted from cart using swipe")




