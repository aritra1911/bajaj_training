from typing import Generator

def count(n: int) -> Generator[int, int, None]:
    i = 1
    while i <= n:
        yield i
        i += 1

def main() -> None:
    for i in count(100):
        print(i)

if __name__ == '__main__':
    main()