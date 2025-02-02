from selenium.webdriver.common.by import By

from PageObjects.ShopHomePage import ShopHomePage


class HomePage:

    shop_link_element = (By.LINK_TEXT , "Shop")
    name = (By.CSS_SELECTOR , "input[name='name']")
    email = (By.NAME , "email")
    password = (By.ID , "exampleInputPassword1")
    checkbox= (By.ID, "exampleCheck1")
    radio_btn = (By.ID, "inlineRadio1")
    submit_btn = (By.CSS_SELECTOR, "input[type='submit']")
    msg_text = (By.CSS_SELECTOR,"div .alert-success")
    select_gender = (By.ID, "exampleFormControlSelect1")

    def __init__(self,driver):
        self.driver = driver

    def shop_link(self):
         self.driver.find_element(*HomePage.shop_link_element).click()
         shop_page = ShopHomePage(self.driver)
         return shop_page

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)


    def click_radio_btn(self):
        return self.driver.find_element(*HomePage.radio_btn)


    def get_password(self):
        return self.driver.find_element(*HomePage.password)


    def click_checkBox(self):
        return self.driver.find_element(*HomePage.checkbox)


    def click_submit_btn(self):
        return self.driver.find_element(*HomePage.submit_btn)


    def get_msg_text(self):
        return self.driver.find_element(*HomePage.msg_text)


    def get_select_gender(self):
        return self.driver.find_element(*HomePage.select_gender)