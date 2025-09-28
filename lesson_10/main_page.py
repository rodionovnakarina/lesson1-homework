"""
Главная страница сайта.
"""

from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open(self, url: str) -> None:
        """Открыть главную страницу."""
        self.driver.get(url)
