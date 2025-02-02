import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

driver.switch_to.frame("mce_0_ifr")
time.sleep(5)
driver.find_element(By.XPATH, "//button[@class='tox-notification__dismiss tox-button tox-button--naked tox-button--icon']//div").click()
time.sleep(5)
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Hello World!!!")

time.sleep(5)
