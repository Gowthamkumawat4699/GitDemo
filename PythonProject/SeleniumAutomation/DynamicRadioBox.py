from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

radioboxes = driver.find_elements(By.NAME, "radioButton")


#if we know the which radio button need to select then we can use the index number from the webelements to click
radioboxes[1].click()

print(radioboxes[2].is_selected())