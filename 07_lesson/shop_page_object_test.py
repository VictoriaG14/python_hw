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

def test_shop():
    driver = webdriver.Firefox()
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_page.authorize()
    main_page = MainPage(driver)
    wait = WebDriverWait(driver, 10)
    main_page.add_items()
    main_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.checkout()
    order_form = OrderForm(driver)
    order_form.fill_form()
    total_amount = order_form.check_total_price()
    driver.quit()
    assert total_amount == "58.29"


