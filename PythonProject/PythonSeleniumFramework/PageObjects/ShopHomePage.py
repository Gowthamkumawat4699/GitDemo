from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckoutPage


class ShopHomePage:

    products = (By.CSS_SELECTOR , "div[class='card h-100']")
    mobile_names = (By.CSS_SELECTOR , "h4")
    add_link = (By.CSS_SELECTOR , "div button")
    checkoutbutton = (By.CSS_SELECTOR , "li[class='nav-item active']")


    def __init__(self, driver):
        self.driver = driver


    def get_products(self):
        return self.driver.find_elements(*ShopHomePage.products)

    def get_mobile_names(self,driver):
        return driver.find_element(*ShopHomePage.mobile_names)


    def add_button(self,driver):
        return driver.find_element(*ShopHomePage.add_link)


    def checkout_btn(self):
        self.driver.find_element(*ShopHomePage.checkoutbutton).click()
        checkout = CheckoutPage(self.driver)
        return checkout