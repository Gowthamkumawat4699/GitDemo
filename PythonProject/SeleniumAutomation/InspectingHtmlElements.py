import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()
#print(driver.page_source)
print(driver.title)
print(driver.current_url)

# Locators - ID, name , xpath, CSSSelector, className, linkText

# CSS Selector - tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahulshetty")

# Name locator
driver.find_element(By.NAME, "email").send_keys("rahulshettyacademy@gmail.com")
# ID Locator
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Password@123")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
# driver.find_element(By.XPATH, "//h4//input").send_keys("RahulShetty")

# Xpath index number to find web element from multiple elements
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Academy")
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()



# xpath - //tagname[@attribute="value"]
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//input[@value='Submit']").click()

#Class Name locator
text_msg = driver.find_element(By.CLASS_NAME, "alert").text
print(text_msg)
assert "Success" in text_msg

time.sleep(3)
driver.quit()
