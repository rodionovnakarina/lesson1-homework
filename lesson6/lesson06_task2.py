# 06_lesson/lesson06_task2.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("http://uitestingplayground.com/textinput")

    inp = driver.find_element(By.ID, "newButtonName")
    btn = driver.find_element(By.ID, "updatingButton")

    inp.clear()
    inp.send_keys("SkyPro")
    btn.click()

    # Ждём, пока текст кнопки станет "SkyPro"
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )
    print(btn.text)  # ожидается: SkyPro
finally:
    driver.quit()
