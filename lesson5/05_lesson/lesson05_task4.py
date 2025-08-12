from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запускаем Firefox
driver = webdriver.Firefox()

# Переходим на страницу
driver.get("http://the-internet.herokuapp.com/login")

# Ждём загрузку страницы
time.sleep(1)

# Вводим логин
driver.find_element(By.ID, "username").send_keys("tomsmith")

# Вводим пароль
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Нажимаем кнопку Login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Ждём появления текста
time.sleep(1)

# Получаем и выводим текст с зелёной плашки
success_message = driver.find_element(By.ID, "flash").text
print(success_message)

# Закрываем браузер
driver.quit()
