from selenium.webdriver.common.by import By

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.calculator.net/"

    def open(self):
        self.driver.get(self.url)

    def enter_number(self, number):
        for digit in str(number):
            self.driver.find_element(By.XPATH, f"//span[text()='{digit}']").click()

    def press_plus(self):
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()

    def press_equals(self):
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def get_result(self):
        return self.driver.find_element(By.ID, "sciOutPut").text.strip()
