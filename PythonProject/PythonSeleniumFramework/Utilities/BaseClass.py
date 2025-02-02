import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('setup')
class BaseClass:


    def webdriver_wait(self,text):
        wait = WebDriverWait(self.driver ,10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))



    def select_by_visible_text1(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self) :
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandlerObj = logging.FileHandler('logfile.log')
        logger.addHandler(fileHandlerObj)
        formats = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandlerObj.setFormatter(formats)
        logger.setLevel(logging.DEBUG)
        return logger