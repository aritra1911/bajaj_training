def main():
    for j in range(3):
        for _ in range(3-j-1):
            print(end=' ')
        for _ in range(j + 1):
            print(end='* ')
        print()

if __name__ == '__main__':
    main()
