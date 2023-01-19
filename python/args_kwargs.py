import pdb

def my_func(*args, **kwargs) -> None:
    print(type(args), type(kwargs))
    print(args, kwargs)

    pdb.set_trace()

    for arg in args:
        print(arg, end=' ')
    print()

    pdb.set_trace()

    for key, value in kwargs.items():
        print(key, '=', value)

def main() -> None:
    my_func(1, 2, 3, 4, 5, x=4, y=6, z=10)

if __name__ == '__main__':
    main()