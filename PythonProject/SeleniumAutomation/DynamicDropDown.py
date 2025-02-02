from datetime import time
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

webdriver = webdriver.Chrome()
webdriver.get("http://www.rahulshettyacademy.com/dropdownsPractise/")
webdriver.maximize_window()
webdriver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(3)

countries = webdriver.find_elements(By.CSS_SELECTOR, ".ui-menu-item")

for country in countries:
    if country.text == "India":
        country.click()
        assert webdriver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"


# if we select tthe value from the dynamic result then .text doesn't work so we need to use this .get_attribute('value') to extract text from the textbox
print(webdriver.find_element(By.ID, "autosuggest").get_attribute("value"))

