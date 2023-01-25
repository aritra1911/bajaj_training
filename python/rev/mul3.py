def main() -> None:
    l = list(range(1, 51))
    print(l)
    mul3 = list(filter(lambda x: x % 3 == 0, l))
    print(mul3)

if __name__ == '__main__':
    main()