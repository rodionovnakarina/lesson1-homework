from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_submission(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")

    driver.find_element(By.NAME, "my-text").send_keys("Test text")
    driver.find_element(By.NAME, "my-password").send_keys("12345")

    submit_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
    )
    submit_btn.click()

    message = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    assert "Form submitted" in message.text
