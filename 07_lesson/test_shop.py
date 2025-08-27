import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shop(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    add_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    add_btn.click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    checkout_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_btn.click()

    # Проверка URL после перехода на страницу checkout
    WebDriverWait(driver, 15).until(
        lambda d: "/checkout-step-one.html" in d.current_url
    )
    assert "/checkout-step-one.html" in driver.current_url
