from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открываем Chrome
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Кликаем на синюю кнопку
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

    time.sleep(2)  # ждём, чтобы увидеть результат
finally:
    driver.quit()  # закрываем браузер

