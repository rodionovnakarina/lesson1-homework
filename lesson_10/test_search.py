import allure

@allure.title("Проверка поиска")
@allure.description("Тест поиска на сайте")
@allure.feature("Search")
@allure.severity(allure.severity_level.NORMAL)
def test_search(driver):
    with allure.step("Открываем страницу"):
        driver.get("https://example.com")

    with allure.step("Проверяем заголовок"):
        assert "Example" in driver.title
