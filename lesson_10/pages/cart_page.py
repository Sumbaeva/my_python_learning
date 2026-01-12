"""
Page Object для страницы корзины.
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    """
    Класс страницы корзины.
    :param CHECKOUT_BTN: локатор кнопки оформления заказа
    """

    CHECKOUT_BTN = (By.ID, "checkout")

    def checkout(self) -> None:
        """Нажимает кнопку Checkout."""
        self.click(self.CHECKOUT_BTN)
