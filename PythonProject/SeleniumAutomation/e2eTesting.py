import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get('http://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Shop").click()
#driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
#driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()

# windows_ids = driver.window_handles
# driver.switch_to.window(windows_ids[1])

products = driver.find_elements(By.CSS_SELECTOR,"div[class='card h-100']")

for product in products:
    mobile_names = product.find_element(By.CSS_SELECTOR, "h4").text
    if mobile_names == "Blackberry":
        product.find_element(By.CSS_SELECTOR, "div button").click()

driver.execute_script('window.scrollBy(0,500)')

driver.find_element(By.CSS_SELECTOR, "li[class='nav-item active']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.ID, "country").send_keys("Bangalore")
#time.sleep(6)
driver.find_element(By.ID, "country").clear()
driver.find_element(By.ID, 'country').send_keys('Ind')
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox']").click()
driver.find_element(By.CSS_SELECTOR,"input[class*='btn-success']").click()

mgs = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text

assert 'Success' in mgs