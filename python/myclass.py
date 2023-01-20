from abc import ABC, abstractmethod

class MyClass(ABC):
    @abstractmethod
    def calc(self, x: float) -> None:
        pass

class SubClass(MyClass):
    def calc(self, x: float) -> None:
        print('Square =', x ** 2.)

def main():
    ob = SubClass()
    ob.calc(13)

if __name__ == '__main__':
    main()