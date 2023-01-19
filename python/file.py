def main():
    f = open('python/test.txt', 'w')
    f.write('This is a demo file\n')
    f.write('Second line\n')
    f.close()

    f = open('python/test.txt', 'r')
    line = f.readline(); f.seek(0, 0)
    content = f.read(); f.seek(0, 0)
    chars = f.read(10); f.seek(0, 0)
    lines = f.readlines(); f.seek(0, 0)
    f.close()

    print('line :', line)
    print('content :', content)
    print('chars :', chars)
    print('lines :', lines)

if __name__ == '__main__':
    main()
