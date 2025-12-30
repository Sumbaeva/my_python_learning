from selenium import webdriver
from pages.calculator_page import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()
    try:
        delay_value = 45
        calc_page = CalculatorPage(driver, delay=delay_value)
        calc_page.open()
        calc_page.set_delay()
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        result_text, actual_delay = (
            calc_page.wait_for_result_and_measure_time()
        )
        assert result_text == "15"
        assert int(actual_delay) == delay_value
        print("Тест пройден успешно!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()
