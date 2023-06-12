from ..src.calculator import Calculator
from ..src.exceptions.calculatorError import CalculatorError
import pytest

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize("a, b, expected_result", [
    (5, 3, 8),
    (-5, -3, -8),
    (5, 0, 5)
])
def test_add(calculator, a, b, expected_result):
    result = calculator.add(a, b)
    assert result == expected_result

@pytest.mark.parametrize("a, b, expected_result", [
    (5, 3, 2),
    (-5, -3, -2)
])
def test_subtract(calculator, a, b, expected_result):
    result = calculator.subtract(a, b)
    assert result == expected_result

@pytest.mark.parametrize("a, b, expected_result", [
    (5, 3, 15),
    (-5, -3, 15),
    (5, 0, 0)
])
def test_multiply(calculator, a, b, expected_result):
    result = calculator.multiply(a, b)
    assert result == expected_result

def test_divide(calculator):
    result = calculator.divide(6, 3)
    assert result == 2

def test_divide_by_zero(calculator):
    with pytest.raises(CalculatorError) as context:
        calculator.divide(6, 0)

    assert str(context.value) == "Can't divide by Zero"

def test_check_input_valid_number(calculator):
    calculator._check_inputs(5)  # No exception should be raised

def test_check_input_invalid_number(calculator):
    with pytest.raises(CalculatorError) as context:
        calculator._check_inputs("two")

    assert str(context.value) == '"two" is not a valid number'




# @pytest.fixture
# def calculator():
#     return Calculator()

# def test_add(calculator):
#     result = calculator.add(5, 3)
#     assert result == 8

# def test_add_negative_numbers(calculator):
#     result = calculator.add(-5, -3)
#     assert result == -8

# def test_add_zero(calculator):
#     result = calculator.add(5, 0)
#     assert result == 5

# def test_subtract(calculator):
#     result = calculator.subtract(5, 3)
#     assert result == 2

# def test_subtract_negative_numbers(calculator):
#     result = calculator.subtract(-5, -3)
#     assert result == -2

# def test_multiply(calculator):
#     result = calculator.multiply(5, 3)
#     assert result == 15

# def test_multiply_negative_numbers(calculator):
#     result = calculator.multiply(-5, -3)
#     assert result == 15

# def test_multiply_by_zero(calculator):
#     result = calculator.multiply(5, 0)
#     assert result == 0

# def test_divide(calculator):
#     result = calculator.divide(6, 3)
#     assert result == 2

# def test_divide_by_zero(calculator):
#     with pytest.raises(CalculatorError) as context:
#         calculator.divide(6, 0)

#     assert str(context.value) == "Can't divide by Zero"

# def test_check_input_valid_number(calculator):
#     calculator._check_input(5)  # No exception should be raised

# def test_check_input_invalid_number(calculator):
#     with pytest.raises(CalculatorError) as context:
#         calculator._check_input("two")

#     assert str(context.value) == '"two" is not a valid number'


# from ..src.calculator import Calculator
# from ..src.exceptions.calculatorError import CalculatorError
# import pytest

# def test_add():
#     calculator = Calculator()

#     result = calculator.add(5, 3)

#     assert result == 8

# def test_subtract():
#     calculator = Calculator()

#     result = calculator.subtract(5, 3)

#     assert result == 2

# def test_multiply():
#     calculator = Calculator()

#     result = calculator.multiply(5, 3)

#     assert result == 15

# def test_divide():
#     calculator = Calculator()

#     result = calculator.divide(6, 3)

#     assert result == 2

# def test_add_with_strings():
#     calculator = Calculator()

#     with pytest.raises(CalculatorError) as context:
#         calculator.add("two", "four")

#     assert str(context.value) == '"two" is not a valid number'