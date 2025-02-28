class Calc:

    def add(self, a, b):
        return a + b

    def subtract(self,a, b):
        return a - b

    def multiply(self,a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Nie można dzielić przez zero")
        return a / b


calc = Calc()
#print(calc.add(3, 2))
#print(calc.subtract(3, 2))
