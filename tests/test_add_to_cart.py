import pytest
from conftest import appium_driver, logger
from pages import (
    SauceDemoLoginPage,
    SauceDemoPlpPage
)


class TestAddToCart:

    @pytest.fixture(autouse=True)
    def setup(self, appium_driver):
        """Setup method to initialize page objects before each test."""
        logger.info("Initializing page objects for the test.")
        self.login_page = SauceDemoLoginPage(appium_driver)
        self.plp_page = SauceDemoPlpPage(appium_driver)

    def test_add_to_cart(self):
        """Test the functionality of adding a product to the cart."""
        logger.info("Starting test: test_add_to_cart")

        # Enter username and password to log in
        self.login_page.enter_username()
        logger.info("Username entered.")

        self.login_page.enter_password()
        logger.info("Password entered.")

        self.login_page.click_on_login_button()
        logger.info("Login button clicked.")

        # Add product to the cart
        self.plp_page.add_product_to_cart()
        logger.info("Product added to cart.")

        # Get the cart count and assert it
        cart_count = self.plp_page.get_cart_count()
        logger.info(f"Retrieved cart count: {cart_count}")

        # Assert that the cart count is as expected
        assert cart_count == "1", f"Expected cart count to be '1', but got '{cart_count}'."
        logger.info("Test completed successfully. Product added to cart.")
