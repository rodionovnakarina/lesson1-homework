from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product(self, name):
        self.driver.find_element(By.XPATH, f"//div[text()='{name}']/ancestor::div[@class='inventory_item']//button").click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first = (By.ID, "first-name")
        self.last = (By.ID, "last-name")
        self.zip = (By.ID, "postal-code")
        self.cont = (By.ID, "continue")
        self.total = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first, last, zip_code):
        self.driver.find_element(*self.first).send_keys(first)
        self.driver.find_element(*self.last).send_keys(last)
        self.driver.find_element(*self.zip).send_keys(zip_code)
        self.driver.find_element(*self.cont).click()

    def get_total(self):
        return self.driver.find_element(*self.total).text
