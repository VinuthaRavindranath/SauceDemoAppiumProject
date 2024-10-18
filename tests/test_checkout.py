import pytest
from conftest import appium_driver, logger
from constants import AppConstants
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

    @pytest.mark.usefixtures("appium_driver", "log_on_failure")
    def test_checkout(self):
        """Test the functionality of adding a product to the cart and completing the checkout process."""
        logger.info("Starting test: test_checkout")

        # Perform login
        self.login_page.do_login(AppConstants.STANDARD_USER, AppConstants.STANDARD_PASSWORD)

        # Add a product to the cart
        self.plp_page.add_product_to_cart()  # Add a product from the product list page
        logger.info("Product added to cart.")

        # Navigate to the cart
        self.plp_page.click_on_mini_cart()  # Click on the mini cart icon

        # Proceed to checkout
        self.cart_page.click_on_checkout_button()  # Click the checkout button

        # Fill out the checkout information
        self.checkout_page.enter_first_name(AppConstants.FIRST_NAME)  # Enter first name
        self.checkout_page.enter_last_name(AppConstants.LAST_NAME)  # Enter last name
        self.checkout_page.enter_postal_code(AppConstants.POSTAL_CODE)  # Enter postal code
        self.checkout_page.click_on_continue_button()  # Click continue to proceed

        # Complete the checkout process
        self.checkout_page.click_on_finish_button()  # Click finish to finalize the order

        # Validate that the order confirmation page is displayed
        self.order_confirmation_page.validate_presence_of_checkout_complete()
