import pytest
from conftest import appium_driver, logger
from pages import (
    SauceDemoLoginPage,
    SauceDemoPlpPage,
    SauceDemoCartPage,
    SauceDemoCheckoutPage,
    SauceDemoOrderConfirmationPage,
)


class TestCheckout:

    @pytest.fixture(autouse=True)
    def setup(self, appium_driver):
        """Setup method to initialize page objects before each test."""
        logger.info("Initializing page objects for the test.")

        # Initialize page object instances for the test
        self.login_page = SauceDemoLoginPage(appium_driver)
        self.plp_page = SauceDemoPlpPage(appium_driver)
        self.cart_page = SauceDemoCartPage(appium_driver)
        self.checkout_page = SauceDemoCheckoutPage(appium_driver)
        self.order_confirmation_page = SauceDemoOrderConfirmationPage(appium_driver)

    def test_checkout(self):
        """Test the functionality of adding a product to the cart and completing the checkout process."""
        logger.info("Starting test: test_checkout")

        # Log in to the application
        self.login_page.enter_username()  # Input username
        logger.info("Username entered.")

        self.login_page.enter_password()  # Input password
        logger.info("Password entered.")

        self.login_page.click_on_login_button()  # Click the login button
        logger.info("Login button clicked.")

        # Add a product to the cart
        self.plp_page.add_product_to_cart()  # Add a product from the product list page
        logger.info("Product added to cart.")

        # Navigate to the cart
        self.plp_page.click_on_mini_cart()  # Click on the mini cart icon

        # Proceed to checkout
        self.cart_page.click_on_checkout_button()  # Click the checkout button

        # Fill out the checkout information
        self.checkout_page.enter_first_name()  # Enter first name
        self.checkout_page.enter_last_name()  # Enter last name
        self.checkout_page.enter_postal_code()  # Enter postal code
        self.checkout_page.click_on_continue_button()  # Click continue to proceed

        # Complete the checkout process
        self.checkout_page.click_on_finish_button()  # Click finish to finalize the order

        # Validate that the order confirmation page is displayed
        self.order_confirmation_page.validate_presence_of_checkout_complete()
