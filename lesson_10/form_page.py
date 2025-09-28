"""
Модуль для работы со страницей формы.
"""

from selenium.webdriver.remote.webdriver import WebDriver


class FormPage:
    """Класс страницы формы."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open(self, url: str) -> None:
        """Открыть страницу формы."""
        self.driver.get(url)

    def fill_field(self, locator: tuple, value: str) -> None:
        """Заполнить поле формы."""
        field = self.driver.find_element(*locator)
        field.clear()
        field.send_keys(value)
