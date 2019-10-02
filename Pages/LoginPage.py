import time
from Utils import Utils

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.email_id = "Email"
        self.password_id = "Password"
        self.loginbutton_xpath = "//input[@class ='button-1 login-button']"

    def Login(self):
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, -900);")
        self.driver.find_element_by_id(self.email_id).send_keys(Utils.Email)
        self.driver.find_element_by_id(self.password_id).send_keys(Utils.Password)
        self.driver.find_element_by_xpath(self.loginbutton_xpath).click()
        time.sleep(7)
