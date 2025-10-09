import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Калькулятор")
@allure.severity("critical")
class MainPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.title("Добавление товаров в корзину")
    @allure.severity("critical")
    @allure.feature("Корзина")
    def add_items(self) -> None:
        """
        Это функция добавления товаров в корзину.
        """
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for product_name in products_to_add:
            add_to_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//div[text()='{product_name}']"
                               "/ancestor::div[@class='inventory_item']"
                               "//button[contains(text(), 'Add to cart')]")))
            add_to_cart_button.click()

    @allure.title("Перейти в корзину")
    @allure.severity("critical")
    @allure.feature("Корзина")
    def go_to_cart(self) -> None:
        """
        Переход на страницу корзины.
        """
        cart_icon = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_icon.click()