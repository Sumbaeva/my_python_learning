"""
Page Object для страницы оформления заказа.
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutPage(BasePage):
    """
    Класс страницы checkout.
    :param FIRST_NAME: локатор поля ввода имени
    :param LAST_NAME: локатор поля ввода фамилии
    :param POSTAL_CODE: локатор поля ввода почтового индекса
    :param CONTINUE_BTN: локатор кнопки продолжения
    :param TOTAL_LABEL: локатор элемента с общей суммой
    """

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def fill_shipping(
        self,
        first_name: str,
        last_name: str,
        zip_code: str,
    ) -> None:
        """
        Заполняет форму доставки и нажимает Continue.
        :param first_name: имя
        :param last_name: фамилия
        :param zip_code: почтовый индекс
        """
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.POSTAL_CODE, zip_code)
        self.click(self.CONTINUE_BTN)

    def get_total(self) -> str:
        """
        Возвращает итоговую сумму заказа.
        :return: текст с суммой (строка)
        """
        return self.get_text(self.TOTAL_LABEL)
