import time

from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Top Deals").click()
windows_ids = driver.window_handles
driver.switch_to.window(windows_ids[1])
# driver.find_element(By.CLASS_NAME,"sort-icon sort-ascending").click()
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
browser_sorted_veg_list = []
veg_list = driver.find_elements(By.XPATH , "//tr/td[1]")

for ele in veg_list:
    browser_sorted_veg_list.append(ele.text)


# copy or slice to copy list to another variable
original_browser_sorted_list = browser_sorted_veg_list.copy()
browser_sorted_veg_list.sort()

assert browser_sorted_veg_list == original_browser_sorted_list



