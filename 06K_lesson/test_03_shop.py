from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pytest

class TestSauceDemo:

    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()))
        driver.implicitly_wait(30)
        yield driver
        driver.quit()

    def test_total_amount(self, driver):
        driver.get("https://www.saucedemo.com/")

        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for product_name in products_to_add:
            add_to_cart_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//div[text()='{product_name}']"
                     "/ancestor::div[@class='inventory_item']"
                     "//button[contains(text(), 'Add to cart')]")))
            add_to_cart_button.click()

        cart_icon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_icon.click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
        )

        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )

        first_name_field = driver.find_element(By.ID, "first-name")
        first_name_field.send_keys("Виктория")

        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Габышева")

        postal_code_field = driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys("111111")

        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )

        total_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        total_amount = total_text.replace("Total: $", "")

        assert total_amount == "58.29", (
            f"Итоговая сумма {total_amount} не равна ожидаемой $58.29")

        print(f"Итоговая сумма: ${total_amount} - проверка пройдена")
