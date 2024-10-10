import pytest
import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def appium_driver():
    """
    Fixture to create and manage the Appium driver instance.

    This fixture initializes the Appium driver with specified capabilities and
    ensures it is properly quit after the tests are done.

    Returns:
        WebDriver: The initialized Appium driver instance.
    """
    logger.info("Starting Appium driver setup.")

    # Define desired capabilities for the Appium driver
    capabilities = {
        'platformName': 'Android',  # Specify the platform
        'platformVersion': '15',  # Specify the Android version
        'deviceName': 'emulator-5554',  # Name of the device (emulator)
        'appPackage': 'com.swaglabsmobileapp',  # Package name of the app
        'appActivity': 'com.swaglabsmobileapp.MainActivity',  # Main activity of the app
        'automationName': 'UiAutomator2',  # Automation engine
        'noReset': True  # Do not reset app state before the session
    }

    appium_server_url = 'http://localhost:4723/wd/hub'  # URL of the Appium server
    options = UiAutomator2Options().load_capabilities(capabilities)

    # Create the Appium driver
    driver = webdriver.Remote(command_executor=appium_server_url, options=options)
    logger.info("Appium driver initialized successfully.")

    yield driver  # Provide the driver to the tests

    # Teardown
    logger.info("Quitting Appium driver.")
    driver.quit()  # Quit the driver session
    logger.info("Appium driver quit successfully.")
