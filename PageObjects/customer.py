from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class addcustomer:
    TEXT_MCUSTOMER_XPATH = "//a[@href='#']//p[contains(text(),'Customers')]"
    TEXT_SCUSTOMER_XPATH = "(//a[@class='nav-link'])[22]"
    TEXT_ADD_NEW_XPATH = "//a[normalize-space()='Add new']"
    TEXT_BOX_EMAIL_XPATH = "//input[@id='Email']"
    TEXT_BOX_PASSWORD_XAPTH = "//input[@id='Password']"
    TEXT_BOX_FIRST_NAME_XPATH = "//input[@id='FirstName']"
    TEXT_BOX_LAST_NAME_XPATH = "//input[@id='LastName']"
    BUTTON_GENDER_MALE_XPATH = "//input[@id='Gender_Male']"
    BUTTON_GENDER_FEMALE_XPATH = "//input[@id='Gender_Female']"
    TEXT_BOX_DATE_XPATH = "//input[@id='DateOfBirth']"
    TEXT_BOX_COMPANY_NAME_XPATH = "//input[@id='Company']"
    CHKBOX_TAX_XPATH = "//input[@id='IsTaxExempt']"
    SELECT_CUSTOMER_ROLE_XPATH = "(//div[@role='listbox'])[2]"
    TEXT_REGISTERED_CANCEL_XPATH = "//span[@title='delete']"
    DROP_CUSTOMER_ROLE_XPATH = "//div[@class='k-list-scroller']/child::ul[1]/li"
    SELECT_VENDOR_XPATH = "//select[@id='VendorId']"
    Chkbox_Active_xpath = "//input[@id='Active']"
    BUTTON_SAVE_XPATH = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def maincustomer(self):
        self.driver.find_element(By.XPATH, self.TEXT_MCUSTOMER_XPATH).click()

    def subcustomer(self):
        self.driver.find_element(By.XPATH, self.TEXT_SCUSTOMER_XPATH).click()

    def add_new(self):
        self.driver.find_element(By.XPATH, self.TEXT_ADD_NEW_XPATH).click()

    def email(self, email):
        mail = self.driver.find_element(By.XPATH, self.TEXT_BOX_EMAIL_XPATH)
        mail.clear()
        mail.send_keys(email)

    def password(self, password):
        pass_key = self.driver.find_element(By.XPATH, self.TEXT_BOX_PASSWORD_XAPTH)
        pass_key.clear()
        pass_key.send_keys(password)

    def fname(self, firstname):
        name1 = self.driver.find_element(By.XPATH, self.TEXT_BOX_FIRST_NAME_XPATH)
        name1.clear()
        name1.send_keys(firstname)

    def lname(self, lastname):
        name2 = self.driver.find_element(By.XPATH, self.TEXT_BOX_LAST_NAME_XPATH)
        name2.clear()
        name2.send_keys(lastname)

    def gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.BUTTON_GENDER_MALE_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, self.BUTTON_GENDER_FEMALE_XPATH).click()

    def birthdate(self, dob):
        date = self.driver.find_element(By.XPATH, self.TEXT_BOX_DATE_XPATH)
        date.clear()
        date.send_keys(dob)

    def company(self, companyname):
        name = self.driver.find_element(By.XPATH, self.TEXT_BOX_COMPANY_NAME_XPATH)
        name.clear()
        name.send_keys(companyname)

    def tax(self):
        self.driver.find_element(By.XPATH, self.CHKBOX_TAX_XPATH).click()

    def customer_role(self, role):
        if role == 'Guest' or 'Administrators' or 'Forum Moderators' or 'Vendors':
            self.driver.find_element(By.XPATH, self.TEXT_REGISTERED_CANCEL_XPATH)
        roles = self.driver.find_elements(By.XPATH, self.SELECT_CUSTOMER_ROLE_XPATH)
        for i in roles:
            if i.text == role:
                i.click()

    def vendors(self, vendor):
        ven = Select(self.driver.find_element(By.XPATH, self.SELECT_VENDOR_XPATH))
        ven.select_by_visible_text(vendor)

    def active(self):
        self.driver.find_element(By.XPATH, self.Chkbox_Active_xpath).click()

    def save(self):
        self.driver.find_element(By.XPATH, self.BUTTON_SAVE_XPATH).submit()
