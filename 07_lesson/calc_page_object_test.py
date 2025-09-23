from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.calc_page import CalcPage

def test_calc():
    driver = webdriver.Chrome()
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.set_delay()
    calc_page.click_element()
    calc_page.wait_delay()
    res = calc_page.get_result()
    assert res == '15'

    driver.quit()