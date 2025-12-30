from selenium import webdriver
from pages.calculator_page import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()
    try:
        calc_page = CalculatorPage(driver)
        calc_page.open()
        calc_page.set_delay(45)
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")
        result = calc_page.get_result()
        assert result == "15", f"Ожидался результат 15, получено: {result}"
        print("Тест калькулятора пройден успешно!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()
