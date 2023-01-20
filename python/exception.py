def main() -> None:
    try:
        f = open('/tmp/myfile', 'w')
        a, b = [ int(x) for x in input('Enter two numbers: ').split() ]
        c = a / b
        f.write('Writing %d into file\n' % c)
    except ZeroDivisionError as ze:
        print('Error :', ze)
    finally:
        f.close()

if __name__ == '__main__':
    main()