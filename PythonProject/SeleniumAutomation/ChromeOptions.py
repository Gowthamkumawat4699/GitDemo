from selenium import webdriver
from selenium import *
import selenium
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
# running chrome browser we cannot see tht while run in headless mode
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://www.rahulshettyacademy.com/AutomationPractice/")
print(driver.title)

radioboxes = driver.find_elements(By.NAME, "radioButton")


#if we know the which radio button need to select then we can use the index number from the webelements to click
radioboxes[1].click()

print(radioboxes[2].is_selected())
