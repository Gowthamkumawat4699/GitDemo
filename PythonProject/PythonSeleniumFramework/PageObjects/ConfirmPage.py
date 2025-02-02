from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    loc_txt_ele = (By.ID , "country")
    text_link_ele = (By.LINK_TEXT , "India")
    check_box_ele = (By.CSS_SELECTOR , "div[class*='checkbox']")
    submit_ele = (By.CSS_SELECTOR , "input[class*='btn-success']")
    msg_ele = (By.CSS_SELECTOR , "div[class*='alert-success']")

    def loc_text_box(self):
        return self.driver.find_element(*ConfirmPage.loc_txt_ele)

    def text_link(self):
        return self.driver.find_element(*ConfirmPage.text_link_ele)


    def check_box(self):
        return self.driver.find_element(*ConfirmPage.check_box_ele)

    def submit_btn(self):
        return self.driver.find_element(*ConfirmPage.submit_ele)

    def msg_text(self):
        return self.driver.find_element(*ConfirmPage.msg_ele)