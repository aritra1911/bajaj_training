def main() -> None:
    try:
        name = input('Enter filename: ')
        f = open(name, 'r')
    except IOError as ie:
        print('File doesn\'t exist', ie)
    else:
        n = len(f.readlines())
        print('File has', n, 'lines')

if __name__ == '__main__':
    main()