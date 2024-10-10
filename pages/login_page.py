from appium.webdriver.common.appiumby import AppiumBy
from utils.element_util import ElementUtil
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)


class SauceDemoLoginPage(ElementUtil):

    def __init__(self, driver):
        super().__init__(driver)
        # Element locators
        self.username = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
        self.password = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
        self.login_button = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

    def enter_username(self):
        """
        Enter the username into the username input field.

        This method waits for the username field to be present and then enters the
        predefined username ("standard_user").

        Returns:
            None: This method does not return a value.
        """
        self.wait_for_element(*self.username)
        self.driver.find_element(*self.username).send_keys("standard_user")
        logging.info("Entered username: standard_user")

    def enter_password(self):
        """
        Enter the password into the password input field.

        This method waits for the password field to be present and then enters the
        predefined password ("secret_sauce").

        Returns:
            None: This method does not return a value.
        """
        self.wait_for_element(*self.password)
        self.driver.find_element(*self.password).send_keys("secret_sauce")
        logging.info("Entered password.")

    def click_on_login_button(self):
        """
        Click the login button to submit the login form.

        This method locates the login button and simulates a click action.

        Returns:
            None: This method does not return a value.
        """
        self.driver.find_element(*self.login_button).click()
        logging.info("Clicked on the login button.")

    def do_login(self):
        """
        Perform the complete login process.

        This method sequentially calls the methods to enter the username and password
        and then click the login button.

        Returns:
            None: This method does not return a value.
        """
        logging.info("Performing login.")
        self.enter_username()
        self.enter_password()
        self.click_on_login_button()
        logging.info("Login action completed.")
