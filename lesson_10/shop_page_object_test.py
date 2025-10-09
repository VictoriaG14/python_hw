import allure
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.order_form import OrderForm
import pytest


@allure.title("Онлайн-магазин")
@allure.severity("critical")
def test_shop():
    with allure.step("Открыть браузер"):
        driver = webdriver.Firefox()
    auth_page = AuthPage(driver)
    with allure.step("Перейти на сайт магазина"):
        auth_page.open()
    with allure.step("Авторизация"):
        auth_page.authorize()
    main_page = MainPage(driver)
    wait = WebDriverWait(driver, 10)
    with allure.step("Добавление товаров в корзину"):
        main_page.add_items()
    with allure.step("Перейти на страницу корзины"):
        main_page.go_to_cart()
    cart_page = CartPage(driver)
    with allure.step("Оформление заказа"):
        cart_page.checkout()
    order_form = OrderForm(driver)
    with allure.step("Заполнить персональные данные в поля"):
        order_form.fill_form()
    with allure.step("Проверка итоговой суммы"):
        total_amount = order_form.check_total_price()
    driver.quit()
    with allure.step("Сравнить итоговую сумму со значением '58.29'"):
        assert total_amount == "58.29"
