from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CalculatorPage(BasePage):
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")

    def __init__(self, driver):
        super().__init__(driver, timeout=45)

    def open(self):
        super().open(self.URL)

    def set_delay(self, delay):
        self.send_keys(self.DELAY_INPUT, str(delay))

    def click_button(self, text):
        locator = (By.XPATH, f"//span[text()='{text}']")
        self.click(locator)

    def get_result(self):
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, "15")
        )
        return self.driver.find_element(*self.SCREEN).text.strip()
