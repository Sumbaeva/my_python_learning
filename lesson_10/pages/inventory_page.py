"""
Page Object для главной страницы магазина (inventory).
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):
    """
    Класс главной страницы магазина.
    :param ADD_BACKPACK: локатор кнопки добавления рюкзака
    :param ADD_BOLT_TSHIRT: локатор кнопки добавления футболки
    :param ADD_ONESIE: локатор кнопки добавления комбинезона
    :param CART_LINK: локатор иконки корзины
    """

    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self) -> None:
        """Добавляет рюкзак в корзину."""
        self.click(self.ADD_BACKPACK)

    def add_bolt_tshirt(self) -> None:
        """Добавляет футболку Bolt в корзину."""
        self.click(self.ADD_BOLT_TSHIRT)

    def add_onesie(self) -> None:
        """Добавляет Onesie в корзину."""
        self.click(self.ADD_ONESIE)

    def go_to_cart(self) -> None:
        """Переходит в корзину по иконке."""
        self.click(self.CART_LINK)
