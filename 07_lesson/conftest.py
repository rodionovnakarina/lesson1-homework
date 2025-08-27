import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Настройки Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # открывать на весь экран
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--ignore-certificate-errors")

    # Инициализация драйвера через webdriver_manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
    yield driver  # возвращаем драйвер в тест

    driver.quit()  # закрываем после теста
