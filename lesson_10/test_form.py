import allure

@allure.title("Проверка формы")
@allure.description("Тест заполнения формы")
@allure.feature("Form")
@allure.severity(allure.severity_level.NORMAL)
def test_form(driver):
    with allure.step("Открываем страницу"):
        driver.get("https://example.com/form")

    with allure.step("Проверяем заголовок"):
        assert "Form" in driver.title
