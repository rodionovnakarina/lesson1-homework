import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from shop_pages import ShopPage  # убедись, что путь правильный

def test_shop(driver):
    shop = ShopPage(driver)
    
    # Открываем страницу магазина
    shop.open()
    
    # Логинимся
    shop.login()
    
    # Добавляем первый товар в корзину
    shop.add_first_item_to_cart()
    
    # Переходим в корзину
    shop.go_to_cart()
    
    # Нажимаем оформить заказ и ждём загрузки страницы checkout
    shop.click_checkout()
    
    # Явное ожидание, чтобы проверить, что мы на странице checkout
    WebDriverWait(driver, 10).until(
        EC.url_contains("/checkout")
    )
    
    assert shop.is_on_checkout_page(), "Не перешли на страницу оформления заказа"
