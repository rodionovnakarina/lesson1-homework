from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search(driver):
    driver.get("https://www.google.com")

    search_box = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Selenium Python")
    search_box.submit()

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "search"))
    )
    assert "Selenium Python" in driver.title
