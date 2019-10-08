import time

from selenium.webdriver.support.wait import WebDriverWait


class OtherItems:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

        self.SoundSpeakers_Linktxt = "Portable Sound Speakers"
        self.Add_to_Cart_xpath = "//input[@id='add-to-cart-button-23']"
        self.shoppingCart_xpath = "//div[@class='header-links']//descendant::span[@class ='cart-label']"

    def SelectSpeakers(self):
        self.driver.find_element_by_partial_link_text(self.SoundSpeakers_Linktxt).click()
        self.driver.execute_script("window.scrollTo(0, 400);")
        time.sleep(3)
        self.driver.find_element_by_xpath(self.Add_to_Cart_xpath).click()
        self.driver.execute_script("window.scrollTo(0, -400);")
        cart_button = WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_xpath(self.shoppingCart_xpath))
        cart_button.click()



