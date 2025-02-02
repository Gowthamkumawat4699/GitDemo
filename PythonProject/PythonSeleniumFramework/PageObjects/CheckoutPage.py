import time

from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver

    checkout_btn = (By.XPATH , "//button[@class='btn btn-success']")



    def check_btn(self):
        self.driver.find_element(*CheckoutPage.checkout_btn).click()
        time.sleep(5)
        conf_pg = ConfirmPage(self.driver)
        return conf_pg