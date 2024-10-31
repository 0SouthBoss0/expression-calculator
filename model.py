class Model:
    def __init__(self):
        self.operations = {"+": self.sum_func,
                           "-": self.sub_func,
                           "*": self.mul_func,
                           "×": self.mul_func,
                           "⋅": self.mul_func,
                           "/": self.div_func,
                           "÷": self.div_func,
                           "^": self.pow_func,
                           "%": self.rem_div_func}

    def sum_func(self, a, b):
        return a + b

    def sub_func(self, a, b):
        return a - b

    def mul_func(self, a, b):
        return a * b

    def div_func(self, a, b):
        return a / b

    def pow_func(self, a, b):
        return a ** b

    def rem_div_func(self, a, b):
        return a % b

    def calculate(self, a, operation, b):
        return operation(a, b)
