import logging
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from typing import Tuple

from utils.element_util import ElementUtil

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
Locator = Tuple[AppiumBy, str]


class GesturesUtil():
    def __init__(self, driver):
        """
        Initializes the ElementUtil with a WebDriver instance.

        Args:
            driver (webdriver.Remote): The Appium WebDriver instance.
        """
        self.driver = driver
        # Initialize ElementUtil
        self.element_util = ElementUtil(driver)

    def drag_and_drop(self, source_locator: Locator, target_locator: Locator):
        """

        :param source_locator:
        :param target_locator:
        :return:

        unit = pixels/sec

        """
        source_element = self.element_util.find_element(source_locator)
        target_element = self.element_util.find_element(target_locator)
        startX = source_element.location['x'] + source_element.size['width'] // 2
        startY = source_element.location['y'] + source_element.size['height'] // 2

        endX = target_element.location['x'] + target_element.size['width'] // 2
        endY = target_element.location['y'] + target_element.size['height'] // 2

        # Step 5: Perform the drag and drop gesture
        self.driver.execute_script('mobile: dragGesture', {
            'startX': startX,
            'startY': startY,
            'endX': endX,
            'endY': endY,
            'speed': 1000  # Adjust the speed of the gesture,
        })

    def swipe_item_left(self, locator):
        """
        Swipe an item left using touch actions.

        :param locator: Locator for the WebElement to swipe left.
        """
        element = self.element_util.find_element(locator)  # Ensure this is the correct WebElement

        if isinstance(element, tuple):
            element = element[0]  # Adjust based on the structure of the tuple if needed

        # Get the element's position and size
        rect = element.rect
        width = rect['width']
        height = rect['height']

        # Create the action chain for swiping left
        action = ActionChains(self.driver)

        # Perform the swipe action
        action.move_to_element(element) \
            .click_and_hold() \
            .pause(0.1) \
            .move_by_offset(-width // 4, 0) \
            .release() \
            .perform()
