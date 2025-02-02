from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


# use the javascript commands in this code
driver.execute_script("window.scrollBy(0,200)")
time_data1 = datetime.now().strftime("'%Y-%m-%d %H-%M-%S'")
filename = "Screenshot_"+ time_data1 +".png"
print(time_data1)
driver.get_screenshot_as_file(filename)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.get_screenshot_as_png()
