import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()
#The below lines code means it gives the index of all opened window ID which is opened by the chrome drive in it order into list
multi_windowOpened = driver.window_handles
# We can switch from parent to child window using the below code by index number 0 index have parent window id and 1 have child window
driver.switch_to.window(multi_windowOpened[1])
txt1 = driver.find_element(By.CSS_SELECTOR,"h3").text
print("Child Window Message: ",txt1)
driver.switch_to.window(multi_windowOpened[0])
txt = driver.find_element(By.TAG_NAME,"h3").text
print("Parent window Message: ",txt)



