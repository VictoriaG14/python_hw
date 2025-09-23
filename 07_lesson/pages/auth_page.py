from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

class AuthPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def authorize(self):
        username_field = self.driver.find_element(By.CSS_SELECTOR, "#user-name")
        username_field.send_keys("standard_user")
        password_field = self.driver.find_element(By.CSS_SELECTOR, "#password")
        password_field.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()