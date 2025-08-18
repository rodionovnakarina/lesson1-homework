# 06_lesson/lesson06_task3.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ждём, пока ВСЕ изображения полностью загрузятся (без sleep)
    WebDriverWait(driver, 20).until(
        lambda d: d.execute_script(
            "return Array.from(document.images).every(img => img.complete && img.naturalWidth>0);"
        )
    )

    third_img = driver.find_element(By.CSS_SELECTOR, "img:nth-of-type(3)")
    print(third_img.get_attribute("src"))
finally:
    driver.quit()
