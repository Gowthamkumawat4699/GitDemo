import time
from selenium.webdriver.common.by import By
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2etesting(self) :
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Click on the shop link")
        shop_page = homepage.shop_link()
        products = shop_page.get_products()
        for product in products :
            mobile_names = shop_page.get_mobile_names(product).text
            log.info("List of mobiles is " + mobile_names)

            if mobile_names == "Blackberry" :
                log.info("Selected product is "+mobile_names)
                shop_page.add_button(product).click()
                break

        checkoutpage = shop_page.checkout_btn()
        conf_pg = checkoutpage.check_btn()
        log.info("Enter the text as Ind")
        conf_pg.loc_text_box().send_keys('Ind')
        self.webdriver_wait("India")
        conf_pg.text_link().click()
        conf_pg.check_box().click()
        conf_pg.submit_btn().click()

        mgs = conf_pg.msg_text().text
        print("Message: ",mgs)

        assert 'Success' in mgs
