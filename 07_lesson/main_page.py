from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.google.com")

    def search(self, query):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )
        search_box.clear()
        search_box.send_keys(query + Keys.RETURN)
        WebDriverWait(self.driver, 10).until(
            EC.title_contains(query.split()[0])
        )
