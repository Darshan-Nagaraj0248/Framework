import string
import random
import time

import pytest
from selenium import webdriver
from PageObjects.LoginPages import LoginPage
from PageObjects.customer import addcustomer
from TestCase.confitest import setup
from Utilities.configuration import ReadConfig
from Utilities.CustomLogger import LogGen


class Test_Customer_page:
    url = ReadConfig.readurl()
    username = ReadConfig.readusername()
    password = ReadConfig.readpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_customer(self, setup):
        self.logger.info("**************Loginstarted***************")
        self.driver = setup
        login_page = LoginPage(self.driver)
        self.driver.get(self.url)
        login_page.enter_username(self.username)
        login_page.enter_password(self.password)
        login_page.click_login_button()
        self.logger.info("**************Login successful***************")

        add_cust_page = addcustomer(self.driver)
        add_cust_page.maincustomer()
        time.sleep(5)
        add_cust_page.subcustomer()
        add_cust_page.add_new()

        email = random_generator() + '@gmail.com'
        add_cust_page.email(email)
        add_cust_page.password("test123")
        add_cust_page.fname("Darshan")
        add_cust_page.lname("Nagaraj")
        add_cust_page.gender("Male")
        add_cust_page.birthdate("28/03/1995")
        add_cust_page.company("XYZ")
        add_cust_page.tax()
        add_cust_page.customer_role("Administrators")
        add_cust_page.vendors("Vendor 2")
        add_cust_page.active()
        add_cust_page.save()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
