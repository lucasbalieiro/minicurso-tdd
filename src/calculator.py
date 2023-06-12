from .exceptions.calculatorError import CalculatorError
from numbers import Number

class Calculator:
    def add(self, a: Number, b: Number) -> Number:
        self._check_inputs(a, b)
        return a + b
    
    def subtract(self, a: Number, b: Number) -> Number:
        self._check_inputs(a, b)
        return a - b
    
    def multiply(self, a: Number, b: Number) -> Number:
        self._check_inputs(a, b)
        return a * b
    
    def divide(self, a: Number, b: Number) -> Number:
        self._check_inputs(a, b)
        if b == 0:
            raise CalculatorError("Can't divide by Zero")
        return a / b
        
    def _check_inputs(self, *inputs: Number) -> None:
        for input in inputs:
            if not isinstance(input, Number):
                raise CalculatorError(f'"{input}" is not a valid number')
