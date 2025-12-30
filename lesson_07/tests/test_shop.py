from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop_purchase():
    driver = webdriver.Firefox()
    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack()
        inventory_page.add_bolt_tshirt()
        inventory_page.add_onesie()
        inventory_page.go_to_cart()
        cart_page = CartPage(driver)
        cart_page.checkout()
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_shipping("Иван", "Петров", "123456")
        total = checkout_page.get_total()
        assert total == "Total: $58.29", \
            f"Ожидалось 'Total: $58.29', получено '{total}'"
        print("Тест магазина пройден успешно!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_shop_purchase()
