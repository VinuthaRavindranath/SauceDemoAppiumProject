import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)


class ElementUtil:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=10):
        """
        Wait for a specific element to be present on the page.

        Args:
            by (str): The method to locate elements (e.g., ACCESSIBILITY_ID).
            value (str): The locator value for the element.
            timeout (int): The maximum time to wait for the element (default is 10 seconds).

        Returns:
            WebElement: The located web element.

        Raises:
            TimeoutException: If the element is not found within the specified timeout.
        """
        logging.info(f"Waiting for element: {value}")
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def wait_for_presence(self, by, value):
        """
        Wait for the presence of a specific element on the page.

        Args:
            by (str): The method to locate elements (e.g., ACCESSIBILITY_ID).
            value (str): The locator value for the element.

        Returns:
            None: This method does not return a value.

        Raises:
            TimeoutException: If the element is not found within the default timeout (10 seconds).
        """
        logging.info(f"Waiting for presence of element: {value}")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))

    def scroll_to_end(self):
        """
        Scroll to the end of a vertically scrollable list in an Android app.

        Args:
            driver: The Appium WebDriver instance.
        """
        try:
            # Scroll to the end of the list
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(5)')
            print("Scrolled to the end of the list.")
        except Exception as e:
            print(f"Error while scrolling: {e}")

    def scroll_to_element(self, element, max_attempts=10):
        """Scroll to an element using UIAutomator and return the element."""
        attempts = 0
        while attempts < max_attempts:
            try:
                # Attempt to find the element by content description
                found_element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                         f'new UiSelector().description("{element}")')
                return found_element  # Return the found element
            except NoSuchElementException:
                # If not found, scroll and increment attempts
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                         'new UiScrollable(new UiSelector()).scrollForward();')
                time.sleep(0.5)  # Wait for the UI to settle
                attempts += 1

        raise Exception(f"Element with description '{element}' not found after {max_attempts} attempts.")