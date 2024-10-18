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

    def pinch(self, locator: Locator, duration: int = 1000, zoom_out: bool = True):
        element = self.element_util.find_element(locator)

        # Get element's position and size
        rect = element.rect
        center_x = rect['x'] + rect['width'] // 2
        center_y = rect['y'] + rect['height'] // 2

        # Define starting positions for two fingers
        offset = 100  # Adjust as needed
        start_finger1 = (center_x - offset, center_y)
        start_finger2 = (center_x + offset, center_y)

        # Create action chains for both fingers
        actions = ActionChains(self.driver)

        if zoom_out:
            # Pinch out (zoom out)
            actions \
                .move_to_element_with_offset(element, start_finger1[0], start_finger1[1]) \
                .click_and_hold() \
                .pause(duration / 2000) \
                .move_to_element_with_offset(element, center_x, center_y) \
                .release()

            actions \
                .move_to_element_with_offset(element, start_finger2[0], start_finger2[1]) \
                .click_and_hold() \
                .pause(duration / 2000) \
                .move_to_element_with_offset(element, center_x, center_y) \
                .release()
        else:
            # Pinch in (zoom in)
            actions \
                .move_to_element_with_offset(element, center_x, center_y) \
                .click_and_hold() \
                .pause(duration / 2000) \
                .move_to_element_with_offset(element, start_finger1[0], start_finger1[1]) \
                .release()

            actions \
                .move_to_element_with_offset(element, center_x, center_y) \
                .click_and_hold() \
                .pause(duration / 2000) \
                .move_to_element_with_offset(element, start_finger2[0], start_finger2[1]) \
                .release()

        # Perform the gesture
        actions.perform()

    def tap(self, locator):
        element = self.driver.find_element(*locator)
        # Tap on the center of the element
        actions = ActionChains(self.driver)
        center_x = element.rect['x'] + element.rect['width'] // 2
        center_y = element.rect['y'] + element.rect['height'] // 2

        print(f"Tapping on element at ({center_x}, {center_y})")
        actions \
            .move_to_element_with_offset(element, center_x, center_y) \
            .click() \
            .perform()

    def zoom(self, locator, zoom_in=True, duration=2000):  # Increased duration
        """
        This piece of code is not working as expected
        Its work in progress
        """
        element = self.driver.find_element(*locator)

        # Get the center of the element
        rect = element.rect
        center_x = rect['x'] + rect['width'] // 2
        center_y = rect['y'] + rect['height'] // 2

        # Define offsets for the pinch gesture
        offset = 150  # Increased offset

        print(f"Element Rect: {rect}")  # Log the element's rectangle
        print(f"Zoom Center: ({center_x}, {center_y})")

        actions = ActionChains(self.driver)

        if zoom_in:
            # Pinch in (zoom in)
            finger1_start = (center_x - offset, center_y)
            finger2_start = (center_x + offset, center_y)
            print(f"Zooming in: Finger 1 starts at {finger1_start}, Finger 2 starts at {finger2_start}")

            actions \
                .move_to_element_with_offset(element, finger1_start[0], finger1_start[1]) \
                .click_and_hold() \
                .pause(duration / 1000) \
                .move_to_element_with_offset(element, center_x, center_y) \
                .release()

            actions \
                .move_to_element_with_offset(element, finger2_start[0], finger2_start[1]) \
                .click_and_hold() \
                .pause(duration / 1000) \
                .move_to_element_with_offset(element, center_x, center_y) \
                .release()
        else:
            # Pinch out (zoom out)
            print(
                f"Zooming out: Finger 1 starts at ({center_x}, {center_y}), Finger 2 starts at ({center_x}, {center_y})")

            actions \
                .move_to_element_with_offset(element, center_x, center_y) \
                .click_and_hold() \
                .pause(duration / 1000) \
                .move_to_element_with_offset(element, center_x - offset, center_y) \
                .release()

            actions \
                .move_to_element_with_offset(element, center_x, center_y) \
                .click_and_hold() \
                .pause(duration / 1000) \
                .move_to_element_with_offset(element, center_x + offset, center_y) \
                .release()

        # Perform the actions
        actions.perform()
        print("Zoom action performed.")
        time.sleep(1)  # Optional: pause to observe the effect
