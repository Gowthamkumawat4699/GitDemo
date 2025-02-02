import time

import pytest
from selenium.webdriver.common.by import By

from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass

from testData.HomePageTestData import HomePageData


class TestTwo(BaseClass):

    def test_submitForm(self,getdata):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("Entered the first name as "+getdata["First_Name"])
        homePage.get_name().send_keys(getdata['First_Name'])
        log.info("Entered the last name as " + getdata["Last_Name"])
        homePage.get_email().send_keys(getdata['Email'])
        log.info("Entered the email as " + getdata["Email"])
        homePage.get_password().send_keys(getdata['Password'])
        log.info("Entered the password as " + getdata["Password"])
        self.select_by_visible_text1(homePage.get_select_gender(), getdata['Gender'])
        log.info("selected gender as " + getdata["Gender"])
        time.sleep(5)
        homePage.click_radio_btn().click()
        homePage.click_submit_btn().click()
        message = homePage.get_msg_text().text
        assert "Success" in message

        self.driver.refresh()


    @pytest.fixture(params=HomePageData.get_test_data('Test Two'))
    def getdata(self,request):
        return request.param








