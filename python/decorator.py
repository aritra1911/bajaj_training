from typing import Callable
def my_decorator(func: Callable[[int, int], int]) -> Callable[[int, int], int]:
    return lambda n1, n2: 10 + func(n1, n2)

@my_decorator
def my_func(n1: int, n2: int) -> int:
    return n1 + n2

def main():
    n1 = int(input('Enter a number: '))
    n2 = int(input('Enter a number: '))
    print(my_func(n1, n2))

if __name__ == '__main__':
    main()