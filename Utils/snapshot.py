import moment
from Utils import Utils
import allure


class snapshot():
    def __init__(self, driver):
        self.driver = driver

    def screenshot(self):
        time = moment.now().strftime("%H-%M-%S_%m-%d-%y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                          attachment_type=allure.attachment_type.PNG)
        self.driver.get_screenshot_as_file(
                "C:/Users/ALOK-PC/PycharmProjects/Pytest_Framework/Screenshot/" + ScreenShotName + ".png")
