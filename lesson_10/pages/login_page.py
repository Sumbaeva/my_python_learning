"""
Page Object для страницы авторизации.
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """
    Класс страницы входа.
    :param URL: адрес страницы авторизации
    :param USERNAME: локатор поля ввода имени пользователя
    :param PASSWORD: локатор поля ввода пароля
    :param LOGIN_BTN: локатор кнопки входа
    """

    URL = "https://www.saucedemo.com/"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def open(self) -> None:
        """Открывает страницу авторизации."""
        super().open(self.URL)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию.
        :param username: логин/имя пользователя
        :param password: пароль
        """
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
