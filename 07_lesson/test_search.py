import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search(driver):
    driver.get("https://www.google.com")
    search_box = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

    # Ждём появления результатов поиска
    results = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3"))
    )
    assert len(results) > 0
