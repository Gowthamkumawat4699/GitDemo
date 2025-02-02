import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Gowtham M")
driver.find_element(By.ID,"alertbtn").click()
time.sleep(4)
alert_msg = driver.switch_to.alert
print(alert_msg.text)
alert_msg.accept()
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Gowtham Kumawat")
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
confirmalert= driver.switch_to.alert
print(confirmalert.text)

confirmalert.dismiss()
