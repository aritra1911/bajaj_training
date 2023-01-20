from math import pi

class Shape:
    def __init__(self, name: str) -> None:
        self.name = name

    def area(self):
        pass

    def fact(self) -> str:
        return '2D Shape'

    def __str__(self) -> str:
        return self.name

class Square(Shape):
    def __init__(self, length: float) -> None:
        super().__init__('Square')
        self.length = length

    def area(self) -> float:
        return self.length ** 2.

    def fact(self) -> str:
        return 'Each angle is at 90 degrees'

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__('Circle')
        self.radius = radius

    def area(self) -> str:
        return pi * self.radius ** 2.

def main():
    a = Square(4.)
    b = Circle(5.6)
    print(b)
    print(b.fact())
    print(a)
    print(a.fact())
    print(b.area())
    print(a.area())

if __name__ == '__main__':
    main()