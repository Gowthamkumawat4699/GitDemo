from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


# use the javascript commands in this code
driver.execute_script("window.scrollBy(0,500)")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")