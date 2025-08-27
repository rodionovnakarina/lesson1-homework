from selenium.webdriver.common.by import By

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay = (By.ID, "delay")
        self.result = (By.CSS_SELECTOR, ".screen")

    def set_delay(self, value):
        self.driver.find_element(*self.delay).clear()
        self.driver.find_element(*self.delay).send_keys(str(value))

    def click_button(self, text):
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    def get_result(self):
        return self.driver.find_element(*self.result).text
