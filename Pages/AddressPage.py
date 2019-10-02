import time


class Address():
    def __init__(self, driver):
        self.driver = driver

        self.BillingAddressContinueBTN_xpath = "//div[@id='billing-buttons-container']//input"
        self.ShipAddressContinueBTN_xpath = "//input[@class='button-1 shipping-method-next-step-button']"

    def continueAddress(self):
        self.driver.find_element_by_xpath(self.BillingAddressContinueBTN_xpath).click()
        self.driver.execute_script("window.scrollTo(0, 400);")
        self.driver.find_element_by_xpath(self.ShipAddressContinueBTN_xpath).click()
        time.sleep(5)
