import pytest
import sys
from Utilities.configuration import *
from selenium import webdriver
from PageObjects.LoginPages import LoginPage
from TestCase.confitest import setup
from Utilities.configuration import ReadConfig
from Utilities.CustomLogger import LogGen


class Test_Login:
    url=ReadConfig.readurl()
    username=ReadConfig.readusername()
    password=ReadConfig.readpassword()
    logger=LogGen.loggen()

    def test_url(self, setup):
        self.logger.info("*************Testing_URL_Started*****************")
        self.driver = setup
        self.driver.get(self.url)
        if self.driver.current_url == "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F":
            assert True
            self.logger.info("*************Testing_URL_Passed*****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "URL_Test.png")
            self.logger.info("*************Testing_URL_Failed*****************")
            assert False
        self.driver.close()

    def test_home_page_title(self, setup):
        self.logger.info("*************Testing_Title_Started*****************")
        self.driver = setup
        self.driver.get(self.url)
        title = self.driver.title
        if title == "Your store. Login":
            assert True
            self.logger.info("*************Testing_Title_Passed*****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Home-Page.png")
            self.logger.info("*************Testing_Title_Failed*****************")
            assert False
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*************Testing_Login_Started*****************")
        self.driver = setup
        self.driver.get(self.url)
        login_page = LoginPage(self.driver)
        login_page.enter_username(self.username)
        login_page.enter_password(self.password)
        login_page.click_checkbox()
        login_page.click_login_button()
        if self.driver.title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*************Testing_Login_Passed*****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Test-Login.png")
            self.logger.info("*************Testing_Login_Failed*****************")
            assert False
        self.driver.close()
