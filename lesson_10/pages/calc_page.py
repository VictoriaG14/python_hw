import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.title("Открыть сайт")
    @allure.severity("blocker")
    @allure.feature("Сайт")
    def open(self) -> None:
        """
        Открывает сайт калькулятора.
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.title("Настройка таймера: ввод цифр")
    @allure.description("Калькулятор выведет результат через указанное время в секундах")
    @allure.severity("normal")
    @allure.feature("Ввод данных")
    def set_delay(self) -> None:
        """
        Настройка таймера.
        """
        timer = self.driver.find_element(By.ID, 'delay')
        timer.clear()
        timer.send_keys('45')

    @allure.title("Настройка калькулятора")
    @allure.description("Ввод чисел и знаков")
    @allure.severity("blocker")
    @allure.feature("Ввод данных")
    def click_element(self) -> None:
        """
        Функция ввода чисел и знаков на калькуляторе
        """
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.title("Ожидание результата")
    @allure.severity("critical")
    def wait_delay(self) -> None:
        """
        Ожидание результата, по истечении времени по таймеру
        """
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

    @allure.title("Получение результата")
    @allure.description("Вывод результата в консоль")
    @allure.severity("critical")
    @allure.feature("Вывод в консоль")
    def get_result(self) -> float:
        """
        Получение результата и его вывод в консоль
        """
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result.text
