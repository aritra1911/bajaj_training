def func(my_list):
    my_list.append(100)

def main():
    l = [-1, 2, 3]
    print(l)
    func(l)
    print(l)

if __name__ == '__main__':
    main()
