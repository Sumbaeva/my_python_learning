"""
Тесты для медленного калькулятора.
Проверяется корректность работы задержки и вычисления результата.
"""
import allure
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@allure.title("Тест медленного калькулятора с задержкой 45 секунд")
@allure.description(
    "Проверяем, что после установки задержки 45 секунд "
    "и последовательного нажатия кнопок 7 + 8 = "
    "результат на экране становится '15' примерно через 45 секунд. "
    "Также измеряется и проверяется реальное время выполнения операции."
)
@allure.feature("Медленный калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator():
    """
    Основной тест на работу калькулятора с задержкой.
    Каждый шаг выделен в Allure.step для детального отчёта.
    При ошибке автоматически делается скриншот.
    """
    driver = webdriver.Chrome()

    try:
        with allure.step("Открываем страницу калькулятора"):
            delay_value = 45
            calc_page = CalculatorPage(driver, delay=delay_value)
            calc_page.open()
            allure.attach(
                "Страница калькулятора открыта",
                name="Открытие страницы",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step(f"Устанавливаем задержку {delay_value} секунд"):
            calc_page.set_delay()
            allure.attach(
                f"Задержка установлена на {delay_value} сек",
                name="Установка задержки",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Нажимаем кнопки: 7 + 8 ="):
            calc_page.click_button("7")
            allure.attach(
                "Нажата кнопка 7",
                name="Кнопка 7",
                attachment_type=allure.attachment_type.TEXT
            )

            calc_page.click_button("+")
            allure.attach(
                "Нажата кнопка +",
                name="Кнопка +",
                attachment_type=allure.attachment_type.TEXT
            )

            calc_page.click_button("8")
            allure.attach(
                "Нажата кнопка 8",
                name="Кнопка 8",
                attachment_type=allure.attachment_type.TEXT
            )

            calc_page.click_button("=")
            allure.attach(
                "Нажата кнопка =",
                name="Кнопка =",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Ждём результат и измеряем реальное время"):
            result_text, actual_delay = (
                calc_page.wait_for_result_and_measure_time()
            )

            allure.attach(
                result_text,
                name="Фактический результат на экране",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                f"{actual_delay:.2f} секунд",
                name="Реальное время выполнения",
                attachment_type=allure.attachment_type.TEXT
            )

            assert result_text == "15", (
                f"Ожидался результат '15', получено '{result_text}'"
            )

            tolerance = 1
            assert abs(int(actual_delay) - delay_value) <= tolerance, (
                f"Задержка ожидалась ~{delay_value} сек (±{tolerance}), "
                f"реальная: {int(actual_delay)} сек"
            )

            allure.attach(
                "Результат и задержка корректны",
                name="Успех проверки",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Делаем скриншот успешного результата"):
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Успешный результат на экране",
                attachment_type=allure.attachment_type.PNG
            )

    except Exception as e:
        with allure.step("Скриншот ошибки"):
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Скриншот момента сбоя",
                attachment_type=allure.attachment_type.PNG
            )
        raise e

    finally:
        with allure.step("Закрываем браузер"):
            driver.quit()
            allure.attach(
                "Браузер закрыт",
                name="Завершение сессии",
                attachment_type=allure.attachment_type.TEXT
            )
