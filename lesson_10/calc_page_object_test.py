import allure
from selenium import webdriver
from pages.calc_page import CalcPage


@allure.title("Калькулятор")
@allure.severity("critical")
def test_calc():
    with allure.step("Открыть браузер"):
        driver = webdriver.Chrome()
    calc_page = CalcPage(driver)
    with allure.step("Перейти на сайт калькулятора"):
        calc_page.open()
    with allure.step("Установка таймер"):
        calc_page.set_delay()
    with allure.step("Настройка калькулятора:ввод элементов"):
        calc_page.click_element()
    with allure.step("Ожидание истечения времени по таймеру"):
        calc_page.wait_delay()
    with allure.step("Получение результата"):
        res = calc_page.get_result()
    with allure.step("Сравнить результат с '15'"):
        assert res == '15'

    driver.quit()
