"""
Модуль для работы со страницей калькулятора.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Класс страницы калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор страницы.

        :param driver: WebDriver
        """
        self.driver = driver

    def open(self, url: str) -> None:
        """
        Открыть страницу калькулятора.

        :param url: str — адрес страницы
        """
        self.driver.get(url)

    def enter_number(self, locator: tuple, number: int) -> None:
        """
        Ввести число в поле.

        :param locator: tuple — локатор поля
        :param number: int — число
        """
        field = self.driver.find_element(*locator)
        field.clear()
        field.send_keys(str(number))
