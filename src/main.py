from calculator import Calculator
from exceptions.calculatorError import CalculatorError

def display_menu():
    print("=== CALCULADORA ===")
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Encerrar a calculadora")

def perform_operation():
    calculator = Calculator()
    choice = input("Digite o número da operação desejada: ")

    if choice == '0':
        print("Encerrando a calculadora...")
        return False

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    try:
        if choice == '1':
            result = calculator.add(num1, num2)
            print("Resultado: ", result)
        elif choice == '2':
            result = calculator.subtract(num1, num2)
            print("Resultado: ", result)
        elif choice == '3':
            result = calculator.multiply(num1, num2)
            print("Resultado: ", result)
        elif choice == '4':
                result = calculator.divide(num1, num2)
                print("Resultado: ", result)
    except CalculatorError as ex:
        print(ex)
    return True


if __name__ =='__main__':
    running = True

    while running:
        display_menu()
        running = perform_operation()

    