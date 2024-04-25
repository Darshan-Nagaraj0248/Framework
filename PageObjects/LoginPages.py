from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    checkbox_remember_me_id = "RememberMe"
    button_login_xpath = "//button[normalize-space()='Log in']"
    button_logout_link_text = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        email_field = self.driver.find_element(By.ID, self.textbox_email_id)
        email_field.clear()
        email_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, self.textbox_password_id)
        password_field.clear()
        password_field.send_keys(password)

    def click_checkbox(self):
        self.driver.find_element(By.ID,self.checkbox_remember_me_id).click()

    def click_login_button(self):
        login_button = self.driver.find_element(By.XPATH, self.button_login_xpath)
        login_button.click()


    def click_logout_button(self):
        logout_button_locator = (By.LINK_TEXT, self.button_logout_link_text)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(logout_button_locator)).click()

