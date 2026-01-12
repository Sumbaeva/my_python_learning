"""
Тесты для магазина SauceDemo.
Проверяется полный цикл покупки: авторизация →
→ добавление товаров → корзина → оформление → проверка суммы.
"""
import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.title("Полный цикл покупки в магазине SauceDemo")
@allure.description(
    "Тест проверяет весь процесс покупки: "
    "авторизация как standard_user, добавление трёх товаров в корзину, "
    "переход в корзину, оформление заказа с данными покупателя и "
    "проверку итоговой суммы $58.29"
)
@allure.feature("Покупка в магазине")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_purchase():
    """
    Основной тест на покупку.
    Все шаги документированы через Allure.step для красивого отчёта.
    """
    driver = webdriver.Firefox()

    try:
        with allure.step("Открываем главную страницу магазина"):
            login_page = LoginPage(driver)
            login_page.open()

        with allure.step("Выполняем авторизацию как standard_user"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавляем товары в корзину"):
            inventory_page = InventoryPage(driver)
            inventory_page.add_backpack()
            allure.attach(
                "Добавлен Sauce Labs Backpack",
                name="Backpack",
                attachment_type=allure.attachment_type.TEXT
            )

            inventory_page.add_bolt_tshirt()
            allure.attach(
                "Добавлена Sauce Labs Bolt T-Shirt",
                name="Bolt T-Shirt",
                attachment_type=allure.attachment_type.TEXT
            )

            inventory_page.add_onesie()
            allure.attach(
                "Добавлен Sauce Labs Onesie",
                name="Onesie",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Переходим в корзину"):
            inventory_page.go_to_cart()

        with allure.step("Нажимаем кнопку Checkout"):
            cart_page = CartPage(driver)
            cart_page.checkout()

        with allure.step("Заполняем форму доставки"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_shipping("Иван", "Петров", "123456")

        with allure.step("Проверяем итоговую сумму"):
            total = checkout_page.get_total()
            expected_total = "Total: $58.29"

            allure.attach(
                total,
                name="Фактическая сумма",
                attachment_type=allure.attachment_type.TEXT
            )

            assert total == expected_total, (
                f"Ожидалась сумма '{expected_total}', получена '{total}'"
            )

            allure.attach(
                "Сумма совпадает с ожидаемой",
                name="Успех проверки суммы",
                attachment_type=allure.attachment_type.TEXT
            )

        allure.step("Тест успешно завершён")

    except Exception as e:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Скриншот ошибки",
            attachment_type=allure.attachment_type.PNG
        )
        raise e

    finally:
        with allure.step("Закрываем браузер"):
            driver.quit()
