from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
search_input = driver.find_element(By.ID, "username")
search_input.send_keys("tomsmith")
search_input = driver.find_element(By.ID, "password")
search_input.send_keys("SuperSecretPassword!")
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()
flash = driver.find_element(By.ID, "flash")
print(flash.text)
driver.quit()
