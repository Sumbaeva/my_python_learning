import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CalculatorPage(BasePage):
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")

    def __init__(self, driver, delay=45, timeout=None):
        if timeout is None:
            timeout = delay + 10
        super().__init__(driver, timeout=timeout)
        self.expected_delay = delay

    def open(self):
        super().open(self.URL)

    def set_delay(self):
        self.send_keys(self.DELAY_INPUT, str(self.expected_delay))

    def click_button(self, text):
        locator = (By.XPATH, f"//span[text()='{text}']")
        self.click(locator)

    def wait_for_result_and_measure_time(self, expected_result="15"):
        start_time = time.time()
        self.click_button("=")
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_result)
        )
        end_time = time.time()
        actual_delay = end_time - start_time
        result_text = self.driver.find_element(*self.SCREEN).text.strip()
        return result_text, actual_delay
