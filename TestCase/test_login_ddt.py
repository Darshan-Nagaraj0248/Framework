import pytest
from Utilities.configuration import ReadConfig
from Utilities.excelfunc import rowcount, greencolor,extractdata,redcolor,insertdata
from PageObjects.LoginPages import LoginPage
from TestCase.confitest import setup
from Utilities.CustomLogger import LogGen
import time


class Test_001_Login:
    url=ReadConfig.readurl()
    log=LogGen.loggen()
    file=r"C:\Users\Darshan Nagaraj\PycharmProjects\frameworkproject\pythonProject3\TestData\User_detail.xlsx"
    sheetname="Sheet1"

    def test_url(self, setup):
        self.log.info("*************Testing_URL_Started*****************")
        self.driver = setup
        self.driver.get(self.url)
        if self.driver.current_url == "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F":
            assert True
            self.log.info("*************Testing_URL_Passed*****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "URL_Test.png")
            self.log.info("*************Testing_URL_Failed*****************")
            assert False
        self.driver.close()

    def test_home_page_title(self, setup):
        self.log.info("*************Testing_Title_Started*****************")
        self.driver = setup
        self.driver.get(self.url)
        title = self.driver.title
        if title == "Your store. Login":
            assert True
            self.log.info("*************Testing_Title_Passed*****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Home-Page.png")
            self.log.info("*************Testing_Title_Failed*****************")
            assert False
        self.driver.close()

    @pytest.mark.regression
    def test_login(self, setup):
        self.log.info("*************Testing_Login_Started*****************")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        self.row=rowcount(self.file,self.sheetname)
        for i in range(2,self.row+1):
            self.username=extractdata(self.file,self.sheetname,i,1)
            self.password=extractdata(self.file,self.sheetname,i,2)
            login_page.enter_username(self.username)
            login_page.enter_password(self.password)
            login_page.click_checkbox()
            login_page.click_login_button()
            time.sleep(5)

            if self.driver.title == "Dashboard / nopCommerce administration":
                insertdata(self.file,self.sheetname,i,3,"Passed")
                greencolor(self.file,self.sheetname,i,3)
                assert True
                self.log.info("*************Testing_Login_Passed*****************")
                login_page.click_logout_button()
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "Test-Login.png")
                self.log.info("*************Testing_Login_Failed*****************")
                insertdata(self.file, self.sheetname, i, 3,"Failed")
                redcolor(self.file, self.sheetname, i, 3)



