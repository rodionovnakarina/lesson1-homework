from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запускаем Chrome
driver = webdriver.Chrome()

# Открываем страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Ждём, чтобы страница успела прогрузиться
time.sleep(1)

# Находим кнопку по её тексту (т.к. ID динамический)
button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")

# Кликаем по кнопке
button.click()

# Ждём, чтобы увидеть результат
time.sleep(2)

# Закрываем браузер
driver.quit()
