import datetime
import time
import selenium
from selenium import webdriver
from selenium.webdriver.ie.service import Service

# the below two lines of code is we need to manually download the corresponding chrome drive from the webside and place the path to the Service
# service_obj = Service("C:\\Users\\91709\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
# webdriver = webdriver.Chrome(service=service_obj)
# webdriver.get("https://google.com")
# time.sleep(5)


#Chrome
# The below one line(driver=webdriver.Chrome() is automatically download corresponding chrome driver for your script.
driver = webdriver.Chrome()
driver.get("http://www.rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(3)
driver.quit()

#Firefox
driver2 = webdriver.Firefox()
driver2.get("http://www.rahulshettyacademy.com/AutomationPractice/")
driver2.maximize_window()
print(driver2.title)
print(driver2.current_url)
time.sleep(3)
driver2.quit()

#Edge
driver3 = webdriver.Edge()
driver3.get("http://www.rahulshettyacademy.com/angularpractice/shop")
driver3.maximize_window()
print(driver3.title)
print(driver3.current_url)
time.sleep(3)
driver3.quit()

driver4 = webdriver.Chrome()
driver4.get("http://www.rahulshettyacademy.com/seleniumPractise/#")
driver4.maximize_window()
print(driver4.title)
print(driver4.current_url)
time.sleep(3)
driver4.quit()