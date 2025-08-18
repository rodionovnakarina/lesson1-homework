# 06_lesson/lesson06_task1.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("http://uitestingplayground.com/ajax")

    # Кликаем синюю кнопку
    driver.find_element(By.ID, "ajaxButton").click()

    # Ждём появления зелёной плашки с текстом
    success = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#content .bg-success"))
    )
    print(success.text)  # ожидается: Data loaded with AJAX get request.
finally:
    driver.quit()
