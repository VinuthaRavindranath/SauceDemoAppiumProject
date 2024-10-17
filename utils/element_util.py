import time
import logging
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
Locator = Tuple[AppiumBy, str]


class ElementUtil:
    """
    Utility class for handling common operations on elements in mobile automation using Appium.
    """

    def __init__(self, driver):
        """
        Initializes the ElementUtil with a WebDriver instance.

        Args:
            driver (webdriver.Remote): The Appium WebDriver instance.
        """
        self.driver = driver
        self.action = ActionBuilder(driver)

    # --- Element Utility Methods ---

    def wait_for_element(self, by, value, timeout=10):
        """
        Waits for a specific element to be present on the page.

        Args:
            by (str): The method to locate elements (e.g., AppiumBy.ID).
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
        Waits for the presence of a specific element on the page.

        Args:
            by (str): The method to locate elements (e.g., AppiumBy.ID).
            value (str): The locator value for the element.

        Returns:
            None: This method does not return a value.

        Raises:
            TimeoutException: If the element is not found within the default timeout (10 seconds).
        """
        logging.info(f"Waiting for presence of element: {value}")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))

    def wait_for_visibility(self, by, value, timeout=10):
        """
        Waits for a specific element to be visible on the page.

        Args:
            by (str): The method to locate elements (e.g., AppiumBy.ID).
            value (str): The locator value for the element.
            timeout (int): The maximum time to wait for visibility (default is 10 seconds).

        Returns:
            WebElement: The located web element.

        Raises:
            TimeoutException: If the element is not visible within the specified timeout.
        """
        logging.info(f"Waiting for visibility of element: {value}")
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))

    def wait_for_clickable(self, by, value, timeout=10):
        """
        Waits for a specific element to be clickable.

        Args:
            by (str): The method to locate elements (e.g., AppiumBy.ID).
            value (str): The locator value for the element.
            timeout (int): The maximum time to wait for the element to be clickable (default is 10 seconds).

        Returns:
            WebElement: The located web element.

        Raises:
            TimeoutException: If the element is not clickable within the specified timeout.
        """
        logging.info(f"Waiting for clickable element: {value}")
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))

    def find_element(self, locator: Locator):
        """
        To find web element
        :param locator: The locator of the element
        :return: WebElement
        """
        return self.driver.find_element(*locator)

    def find_elements(self, locator: Locator):
        """
        Finds multiple elements on the page.

        Args:
            by (str): The method to locate elements (e.g., AppiumBy.CLASS_NAME).
            value (str): The locator value for the elements.

        Returns:
            List[WebElement]: A list of located web elements.
        """
        logging.info(f"Finding elements: {locator}")
        return self.driver.find_elements(*locator)

    def send_keys_to_element(self, locator: Locator, text: str):
        """
        Send keys to the input field
        :param locator: The locator of the element
        :param text: text to be sent to the input field
        """
        element = self.find_element(locator)
        element.send_keys(text)

    def click_on_element(self, locator: Locator):
        """
        To click on the web element
        :param locator: The locator of the element
        :return: None
        """
        element = self.find_element(locator)
        element.click()

    def get_text_of_element(self, locator: Locator):
        """
        To get the text of the web element
        :param locator: The locator of the element
        :return: text of the web element
        """
        element = self.find_element(locator)
        return element.text

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

    def scroll_to_element(self, element,ele_tag, max_attempts=10):
        """Scroll to an element using UIAutomator and return the element."""
        attempts = 0
        while attempts < max_attempts:
            try:
                # Attempt to find the element by content
                found_element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                         f'new UiSelector().{ele_tag}("{element}")')
                return found_element  # Return the found element
            except NoSuchElementException:
                # If not found, scroll and increment attempts
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                         'new UiScrollable(new UiSelector()).scrollForward();')
                time.sleep(0.5)  # Wait for the UI to settle
                attempts += 1

        raise Exception(f"Element with {ele_tag} '{element}' not found after {max_attempts} attempts.")

    # --- Gesture Methods ---

    def tap(self, element):
        """
        Taps on a specified element.

        Args:
            element (WebElement): The web element to tap on.

        Returns:
            None
        """
        self.driver.execute_script("mobile: tap", {"element": element.id})
        logging.info("Tapped on the element.")

    def long_press(self, element):
        """
        Performs a long press on a specified element.

        Args:
            element (WebElement): The web element to long press.

        Returns:
            None
        """
        self.driver.execute_script("mobile: longPress", {"element": element.id})
        logging.info("Long pressed on the element.")





    def zoom(self, element):
        """
        Performs a zoom gesture on a specified element.

        Args:
            element (WebElement): The web element to zoom.

        Returns:
            None
        """
        self.driver.execute_script('mobile: zoom', {'element': element.id})
        logging.info("Performed zoom action.")

    # --- Screenshot Utility ---

    def take_screenshot(self, filename):
        """
        Takes a screenshot of the current screen.

        Args:
            filename (str): The name of the file where the screenshot will be saved.

        Returns:
            None
        """
        self.driver.save_screenshot(filename)
        logging.info(f"Screenshot saved as {filename}.")

    # --- Window Utility Methods ---

    def get_window_size(self):
        """
        Retrieves the current size of the app window.

        Returns:
            dict: A dictionary containing the width and height of the window.
        """
        size = self.driver.get_window_size()
        logging.info(f"Window size: {size}")
        return size

    def accept_alert(self):
        """
        Accepts an alert dialog.

        Returns:
            None: This method does not return a value.

        Raises:
            TimeoutException: If no alert is present.
        """
        alert = self.driver.switch_to.alert
        alert.accept()
        logging.info("Accepted alert.")

    def dismiss_alert(self):
        """
        Dismisses an alert dialog.

        Returns:
            None: This method does not return a value.

        Raises:
            TimeoutException: If no alert is present.
        """
        alert = self.driver.switch_to.alert
        alert.dismiss()
        logging.info("Dismissed alert.")

        # --- Context Switching Methods ---

    def get_contexts(self):
        """
        Retrieves a list of available contexts (e.g., native, web).

        Returns:
            List[str]: A list of available contexts.
        """
        contexts = self.driver.contexts
        logging.info(f"Available contexts: {contexts}")
        return contexts

    def switch_to_context(self, context_name):
        """
        Switches to a specified context.

        Args:
            context_name (str): The name of the context to switch to.

        Returns:
            None
        """
        self.driver.switch_to.context(context_name)
        logging.info(f"Switched to context: {context_name}")

    def switch_to_native_context(self):
        """
        Switches back to the native context.

        Returns:
            None
        """
        self.driver.switch_to.context('NATIVE_APP')
        logging.info("Switched to native context.")

    def switch_to_web_context(self):
        """
        Switches to the first available web context.

        Returns:
            None
        """
        contexts = self.get_contexts()
        for context in contexts:
            if 'WEBVIEW' in context:
                self.switch_to_context(context)
                break
        else:
            logging.warning("No web context available to switch to.")

    def pinch_and_zoom(self, locator: Locator):
        time.sleep(5)

        product_image = self.driver.find_element(*locator)

        self.driver.execute_script('mobile: pinchCloseGesture', {
            'element': product_image.id,
            'percent': 200,  # The amount of zoom in, can be adjusted
            'speed': 500})
        time.sleep(5)

    def wait_for_invisibility_of_element(self, by, value):
        """
        Waits for the presence of a specific element on the page.

        Args:
            by (str): The method to locate elements (e.g., AppiumBy.ID).
            value (str): The locator value for the element.

        Returns:
            None: This method does not return a value.

        Raises:
            TimeoutException: If the element is not found within the default timeout (10 seconds).
        """
        logging.info(f"Waiting for presence of element: {value}")
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element((by, value)))
