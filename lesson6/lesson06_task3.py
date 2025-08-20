# 06_lesson/lesson06_task3.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ждём, пока на странице появятся все изображения
    images = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )

    # Убеждаемся, что их стало хотя бы 4
    while len(images) < 4:
        images = driver.find_elements(By.TAG_NAME, "img")

    # Берём третью картинку (индексация с нуля → это images[2])
    third_img = images[2]
    print(third_img.get_attribute("src"))

finally:
    driver.quit()
