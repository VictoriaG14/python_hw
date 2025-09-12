from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")
my_Button = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
my_Button.send_keys("SkyPro")
blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
blue_button.click()
driver.implicitly_wait(20)
txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(txt)
driver.quit()
