class Animal:
    def __init__(self, animal) -> None:
        self.animal = animal
        print(self.animal, "is an animal")

class Mammal(Animal):
    def __init__(self, mname) -> None:
        print(mname, "is warm blooded")
        super().__init__(mname)

class NonWingedMammal(Mammal):
    def __init__(self, nwmammal) -> None:
        print(nwmammal, "can't swim")
        super().__init__(nwmammal)

class NonMarineMammal(Mammal):
    def __init__(self, nmmammal) -> None:
        print(nmmammal, "can't swim")
        super().__init__(nmmammal)

class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self) -> None:
        print("Dog has four legs")
        super().__init__("Dog")

def main():
    ob = NonWingedMammal("Dog")
    d = Dog()
    print(Dog.mro())

if __name__ == '__main__':
    main()