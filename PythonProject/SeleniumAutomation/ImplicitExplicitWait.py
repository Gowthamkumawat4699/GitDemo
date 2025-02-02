import time

from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("be")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

prices = driver.find_elements( By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum1 = 0
for price in prices:
    sum1 = sum1 + int(price.text)

print(sum1)

total_Amount =driver.find_element(By.CSS_SELECTOR,".totAmt").text

assert sum1 == int(total_Amount)

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,'.promoBtn').click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "promoInfo")))

print(driver.find_element(By.CSS_SELECTOR,'.promoInfo').text)


