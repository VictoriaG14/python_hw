from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_calc():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 60)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator."
            "html")

        delay_input = driver.find_element(By.ID, 'delay')
        delay_input.clear()
        delay_input.send_keys("45")

        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        result = driver.find_element(By.CLASS_NAME, "screen")
        wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        assert result.text == "15", (
            f"Expected '15', but got '{result.text}'"
        )
    finally:
        driver.quit()

