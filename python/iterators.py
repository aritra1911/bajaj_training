class MyIterator:
    def __init__(self, l: int, h: int) -> None:
        self.l = l
        self.h = h

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.l <= self.h:
            self.l += 1
            return self.l - 1
        else:
            raise StopIteration

def main() -> None:
    it = MyIterator(20, 400)
    for i in it:
        print(i)

if __name__ == '__main__':
    main()