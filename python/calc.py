class Calculator:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def get_addition(self) -> int:
        return self.a + self.b

    def get_difference(self) -> int:
        return self.a - self.b

    def get_product(self) -> int:
        return self.a * self.b

    def get_division(self) -> int:
        return self.a // self.b