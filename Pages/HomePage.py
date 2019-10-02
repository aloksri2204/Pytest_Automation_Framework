from selenium.webdriver.common.action_chains import ActionChains
import time

class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.Electronics = "//ul[@class='top-menu notmobile']//a[contains(text(),'Electronics ')]"
        self.Cell_Phones = "//ul[@class='top-menu notmobile']//a[contains(text(),'Cell phones')]"

    def NavigateToCellPhone(self):
        hoverElement = self.driver.find_element_by_xpath(self.Electronics)
        time.sleep(2)
        hover = ActionChains(self.driver)
        hover.move_to_element(hoverElement).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.Cell_Phones).click()
