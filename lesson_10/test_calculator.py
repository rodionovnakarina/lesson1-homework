import allure

@allure.title("Проверка калькулятора")
@allure.description("Тест ввода чисел в калькулятор")
@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    with allure.step("Открываем страницу"):
        driver.get("https://example.com/calculator")

    with allure.step("Проверяем заголовок"):
        assert "Calculator" in driver.title
