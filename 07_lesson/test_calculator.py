from calculator_page import CalculatorPage

def test_calculator(driver):
    calc = CalculatorPage(driver)
    calc.open()
    calc.enter_number(7)
    calc.press_plus()
    calc.enter_number(8)
    calc.press_equals()
    result = calc.get_result()
    assert result == "15", f"Ожидали 15, но получили {result}"
