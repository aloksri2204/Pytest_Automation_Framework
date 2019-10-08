import time

from selenium.webdriver.support.wait import WebDriverWait


class CellPhonePage():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.Nokia_Phone_Linktxt = "Nokia Lumia 1020"
        self.Add_to_Cart_xpath = "//input[@type='button'][@id='add-to-cart-button-20']"
        self.shoppingCart_xpath = "//div[@class='header-links']//descendant::span[@class ='cart-label']"

    def SelectPhone(self):
        self.driver.find_element_by_partial_link_text(self.Nokia_Phone_Linktxt).click()
        self.driver.execute_script("window.scrollTo(0, 400);")
        self.driver.find_element_by_xpath(self.Add_to_Cart_xpath).click()
        self.driver.execute_script("window.scrollTo(0, -400);")
        cart_button = WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_xpath(self.shoppingCart_xpath))
        cart_button.click()



