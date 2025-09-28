"""
Страницы магазина.
"""

from selenium.webdriver.remote.webdriver import WebDriver


class ShopPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def add_to_cart(self, locator: tuple) -> None:
        """Добавить товар в корзину."""
        self.driver.find_element(*locator).click()
