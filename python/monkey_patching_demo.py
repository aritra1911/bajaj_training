import monkey_patching

def monkey_patch_func(self) -> None:
    print('Monkey patch func is called')

def main() -> None:
    monkey_patching.Test.func = monkey_patch_func
    ob = monkey_patching.Test()
    ob.func()

if __name__ == '__main__':
    main()