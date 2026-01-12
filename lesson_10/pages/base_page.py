"""
Базовый класс для всех страниц.
Содержит общие методы взаимодействия с элементами и ожидания.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """
    Базовый класс страницы.
    Инициализирует драйвер и объект ожидания.
    """
    def __init__(self, driver, timeout=10):
        """
        Конструктор класса.
        :param driver: экземпляр WebDriver
        :param timeout: максимальное время ожидания в секундах
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        """
        Открывает указанный URL в браузере.
        :param url: адрес страницы для открытия
        """
        self.driver.get(url)

    def find_element(self, locator: tuple) -> "WebElement":
        """
        Находит элемент на странице.
        :param locator: кортеж (By, значение)
        :return: найденный WebElement
        """
        return self.driver.find_element(*locator)

    def click(self, locator: tuple) -> None:
        """
        Кликает на элемент после ожидания его кликабельности.
        :param locator: локатор элемента (кортеж)
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator: tuple, text: str) -> None:
        """
        Вводит текст в поле после ожидания видимости.
        :param locator: локатор поля ввода (кортеж)
        :param text: текст для ввода
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """
        Возвращает текст элемента после ожидания видимости.
        :param locator: локатор элемента (кортеж)
        :return: текст элемента (строка)
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text.strip()
