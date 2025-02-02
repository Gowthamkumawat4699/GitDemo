from argparse import Action

from selenium import *
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#Firefox
driver2 = webdriver.Chrome()
driver2.get("http://www.rahulshettyacademy.com/AutomationPractice/")
driver2.maximize_window()
print(driver2.title)
print(driver2.current_url)
action = ActionChains(driver2)
action.move_to_element(driver2.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
#action.context_click((driver2.find_element(By.LINK_TEXT, "Top"))).perform()
action.move_to_element(driver2.find_element(By.LINK_TEXT, "Reload")).click().perform()

checkboxes = driver2.find_elements(By.CSS_SELECTOR, "input[type=checkbox]")
action.move_to_element(checkboxes[2]).click().perform()
time.sleep(5)

action.double_click(checkboxes[0]).perform()
time.sleep(5)