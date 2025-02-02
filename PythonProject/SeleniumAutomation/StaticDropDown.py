import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()
#print(driver.page_source)
print(driver.title)
print(driver.current_url)

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")


time.sleep(2)