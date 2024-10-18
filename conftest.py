import allure
import pytest
import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.common.exceptions import InvalidSessionIdException
from allure_commons.types import AttachmentType

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def appium_driver():
    """Fixture to create and manage the Appium driver instance."""
    logger.info("Starting Appium driver setup.")

    capabilities = {
        'platformName': 'Android',
        'platformVersion': '15',
        'deviceName': 'emulator-5554',
        'appPackage': 'com.swaglabsmobileapp',
        'appActivity': 'com.swaglabsmobileapp.MainActivity',
        'automationName': 'UiAutomator2',
        'noReset': True
    }

    appium_server_url = 'http://localhost:4723/wd/hub'
    options = UiAutomator2Options().load_capabilities(capabilities)
    global driver
    try:
        driver = webdriver.Remote(command_executor=appium_server_url, options=options)
        logger.info("Appium driver initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize Appium driver: {e}")
        raise

    yield driver  # Provide the driver to the tests

    # Teardown logic
    if driver:
        try:
            logger.info("Quitting Appium driver.")
            driver.quit()  # Quit the driver session
            logger.info("Appium driver quit successfully.")
        except InvalidSessionIdException:
            logger.warning("Attempted to quit an already terminated session.")
        except Exception as e:
            logger.error(f"Error while quitting Appium driver: {e}")

@pytest.fixture
def log_on_failure(request):
    """
    To capture the screenshot of failed tests
    With the help of allure attach() to attach the screenshot in the report
    """
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
