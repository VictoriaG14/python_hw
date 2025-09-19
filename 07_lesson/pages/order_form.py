from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderForm:

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self):
        first_name_field = self.driver.find_element(By.ID, "first-name")
        first_name_field.send_keys("Виктория")

        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Габышева")

        postal_code_field = self.driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys("111111")

        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_button.click()

    def check_total_price(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )

        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        total_amount = total_text.replace("Total: $", "")
        return total_amount