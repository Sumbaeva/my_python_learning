"""
Конфигурация для Allure-отчётов и фикстур
"""
import pytest
import allure


@pytest.fixture(autouse=True)
def allure_environment():
    """Добавляет информацию об окружении в отчёт Allure."""
    allure.dynamic.description("Тесты PageObject для калькулятора и магазина")
    allure.dynamic.tag("Selenium", "PageObject", "Allure")
