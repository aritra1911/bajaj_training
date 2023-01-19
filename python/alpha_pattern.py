def main():
    k = 0
    for j in range(3):
        for _ in range(j + 1):
            print(chr(65 + k), end=' ')
            k += 1
        print()

if __name__ == '__main__':
    main()
