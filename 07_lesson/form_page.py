from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.NAME, "first-name")
        self.last_name = (By.NAME, "last-name")
        self.address = (By.NAME, "address")
        self.email = (By.NAME, "e-mail")
        self.phone = (By.NAME, "phone")
        self.zip = (By.NAME, "zip-code")
        self.city = (By.NAME, "city")
        self.country = (By.NAME, "country")
        self.job = (By.NAME, "job-position")
        self.company = (By.NAME, "company")
        self.submit = (By.CSS_SELECTOR, "button[type='submit']")

    def fill_form(self):
        self.driver.find_element(*self.first_name).send_keys("Иван")
        self.driver.find_element(*self.last_name).send_keys("Петров")
        self.driver.find_element(*self.address).send_keys("Ленина, 55/3")
        self.driver.find_element(*self.email).send_keys("test@skypro.com")
        self.driver.find_element(*self.phone).send_keys("+7985899998787")
        # zip оставляем пустым
        self.driver.find_element(*self.city).send_keys("Москва")
        self.driver.find_element(*self.country).send_keys("Россия")
        self.driver.find_element(*self.job).send_keys("QA")
        self.driver.find_element(*self.company).send_keys("Skypro")
        self.driver.find_element(*self.submit).click()
