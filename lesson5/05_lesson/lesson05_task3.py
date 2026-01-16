from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запускаем Firefox
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Ждём загрузку страницы
time.sleep(1)

# Находим поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")

# Вводим "Sky"
input_field.send_keys("Sky")
time.sleep(1)

# Очищаем поле
input_field.clear()
time.sleep(1)

# Вводим "Pro"
input_field.send_keys("Pro")
time.sleep(2)

# Закрываем браузер
driver.quit()
