import pytest

from Utils import Utils
from Utils.snapshot import snapshot
from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Pages.Electronics_OthersPage import OtherItems
from Pages.LoginPage import LoginPage
from Pages.CheckOutPage import CheckOut
from Pages.AddressPage import Address
from Pages.PaymentPage import Payment
from Pages.OrderConfirmationPage import OrderConfirmation


@pytest.mark.usefixtures("test_setup")
class Test_SpeakerPurchase():

    def test_HomePage(self):
        driver = self.driver
        driver.get(Utils.URL)
        homeObj = HomePage(driver)
        homeObj.NavigateToOthers()
        snapObj = snapshot(driver)
        snapObj.screenshot()

    def test_Speaker_buy(self):
        driver = self.driver
        cellObj = OtherItems(driver)
        cellObj.SelectSpeakers()
        snapObj = snapshot(driver)
        snapObj.screenshot()

    def test_Cart_validations(self):
        driver = self.driver
        cartObj = CartPage(driver)
        cartObj.cart_validation()
        snapObj = snapshot(driver)
        snapObj.screenshot()

    def test_Login(self):
        driver = self.driver
        loginObj = LoginPage(driver)
        loginObj.Checkout_as_Guest()
        snapObj = snapshot(driver)
        snapObj.screenshot()

    def test_Address(self):
        driver = self.driver
        addressObj = Address(driver)
        addressObj.AddressInput()
        snapObj = snapshot(driver)
        snapObj.screenshot()

    def test_Payment(self):
        driver = self.driver
        paymentObj = Payment(driver)
        paymentObj.PaymentOptions()
        snapObj = snapshot(driver)
        snapObj.screenshot()

    def test_OrderConfirmation(self):
        driver = self.driver
        orderConfObj = OrderConfirmation(driver)
        orderConfObj.OrderConfirmationdetails()
        snapObj = snapshot(driver)
        snapObj.screenshot()