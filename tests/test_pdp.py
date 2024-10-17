import time

import pytest
from conftest import appium_driver, logger
from pages import (
    SauceDemoLoginPage,
    SauceDemoPlpPage, SauceDemoCartPage
)
from constants import AppConstants
from pages.pdp_page import SauceDemoPdpPage


class TestPdp:
    @pytest.fixture(autouse=True)
    def setup(self, appium_driver):
        """Setup method to initialize page objects before each test."""
        logger.info("Initializing page objects for the test.")
        self.login_page = SauceDemoLoginPage(appium_driver)
        self.plp_page = SauceDemoPlpPage(appium_driver)
        self.cart_page = SauceDemoCartPage(appium_driver)
        self.pdp_page=SauceDemoPdpPage(appium_driver)


    # def test_zoom_in_and_zoom_out_of_product_image(self):
    #     logger.info("Starting test: test_zoom_in_and_zoom_out_of_product_image")
    #
    #     # Perform login
    #     self.login_page.do_login(AppConstants.STANDARD_USER, AppConstants.STANDARD_PASSWORD)
    #
    #     self.plp_page.click_on_first_product()
    #     self.pdp_page.zoom_product_image()
    #     time.sleep(3)