"""
Page Object для страницы медленного калькулятора.
Позволяет устанавливать задержку, нажимать кнопки и измерять время результата.
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CalculatorPage(BasePage):
    """
    Класс для работы со страницей калькулятора.
    :param URL: адрес страницы калькулятора
    :param DELAY_INPUT: локатор поля ввода задержки
    :param SCREEN: локатор экрана калькулятора
    """

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")

    def __init__(self, driver, delay: int = 45, timeout: int | None = None):
        """
        Инициализация страницы.
        :param driver: экземпляр WebDriver
        :param delay: значение задержки в секундах (по умолчанию 45)
        :param timeout: максимальное время ожидания (по умолчанию delay)
        """
        if timeout is None:
            timeout = delay
        super().__init__(driver, timeout=timeout)
        self.expected_delay = delay

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        super().open(self.URL)

    def set_delay(self) -> None:
        """Вводит заданное значение задержки в поле."""
        self.send_keys(self.DELAY_INPUT, str(self.expected_delay))

    def click_button(self, text: str) -> None:
        """
        Нажимает кнопку с указанным текстом.
        :param text: текст на кнопке ('7', '+', '=' и т.д.)
        """
        locator = (By.XPATH, f"//span[text()='{text}']")
        self.click(locator)

    def wait_for_result_and_measure_time(
        self,
        expected_result: str = "15"
    ) -> tuple[str, float]:
        """
        Нажимает '=', ждёт появления результата и измеряет время.
        :param expected_result: ожидаемый текст на экране
        :return: текст результата, реальное время в секундах (кортеж)
        """
        start_time = time.time()
        self.click_button("=")
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_result)
        )
        end_time = time.time()
        actual_delay = end_time - start_time
        result_text = self.driver.find_element(*self.SCREEN).text.strip()
        return result_text, actual_delay
