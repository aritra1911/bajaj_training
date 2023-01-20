class Book1:
    def __init__(self, pages: int) -> None:
        self.pages = pages

    def __add__(self, another_book) -> int:
        return self.pages + another_book.pages

    def __gt__(self, another_book) -> bool:
        return self.pages > another_book.pages

class Book2:
    def __init__(self, pages: int) -> None:
        self.pages = pages

def main():
    b1 = Book1(100)
    b2 = Book2(500)
    print("Total pages =", b1 + b2)
    if b1 > b2: print("b1 has more pages")
    else: print("b2 may have more pages")

if __name__ == '__main__':
    main()