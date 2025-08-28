from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.url)

    def login(self, username="standard_user", password="secret_sauce"):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def add_first_item_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def click_checkout(self):
        checkout_btn = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()

    def is_on_checkout_page(self):
        return "checkout-step-one.html" in self.driver.current_url
