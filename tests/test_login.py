import pytest
from conftest import appium_driver, logger
from pages import (
    SauceDemoLoginPage,
    SauceDemoPlpPage
)


class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, appium_driver):
        """Setup method to initialize the login page object before each test."""
        logger.info("Initializing SauceDemoLoginPage.")
        self.login_page = SauceDemoLoginPage(appium_driver)
        self.plp_page = SauceDemoPlpPage(appium_driver)

    def test_login(self):
        """Test the login functionality of the Sauce Labs app."""
        logger.info("Starting test: test_login")

        # Enter username
        self.login_page.enter_username()

        # Enter password
        self.login_page.enter_password()

        # Click the login button
        self.login_page.click_on_login_button()

        # Validate that the first product is present after logging in
        self.plp_page.validate_presence_of_first_product()
        logger.info("First product presence validated after login.")
