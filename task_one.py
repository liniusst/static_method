class Calculator:
    @classmethod
    def factorial(cls, number: int) -> int:
        factorial = 1
        for num in range(1, number+1):
            factorial = factorial * num
        return factorial

print(f"Factorial: {Calculator.factorial(number= 5)}")