import allure

@allure.title("Проверка магазина")
@allure.description("Тест добавления товара в корзину")
@allure.feature("Shop")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop(driver):
    with allure.step("Открываем страницу магазина"):
        driver.get("https://example.com/shop")

    with allure.step("Проверяем заголовок"):
        assert "Shop" in driver.title
