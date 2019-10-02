import time


class CellPhonePage():
    def __init__(self, driver):
        self.driver = driver

        self.Nokia_Phone_Linktxt = "Nokia Lumia 1020"
        self.Add_to_Cart_xpath = "//input[@type='button'][@id='add-to-cart-button-20']"
        self.add_to_cart_xpath = "//div[@class='header-links']//descendant::span[@class ='cart-label']"

    def SelectPhone(self):
        self.driver.find_element_by_partial_link_text(self.Nokia_Phone_Linktxt).click()
        self.driver.execute_script("window.scrollTo(0, 400);")
        time.sleep(3)
        self.driver.find_element_by_xpath(self.Add_to_Cart_xpath).click()
        time.sleep(7)
        self.driver.execute_script("window.scrollTo(0, -400);")
        self.driver.find_element_by_xpath(self.add_to_cart_xpath).click()


