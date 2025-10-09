import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


allure.feature("Shop")
class CartPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.title("Оформление заказа")
    @allure.description("Заполнение полей для оформления заказа")
    @allure.severity("critical")
    def checkout(self) -> None:
        """
        Это функция проверки итоговой суммы
        """
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
