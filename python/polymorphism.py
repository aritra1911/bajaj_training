class Cat:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def info(self):
        print(f'Hi!  I am a cat, my name is {self.name} and I am {self.age} years old.')

    def speak(self):
        print("meow!")

class Dog:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def info(self):
        print(f'Hi!  I am a dog, my name is {self.name} and I am {self.age} years old.')

    def speak(self):
        print("Bark!")

def main():
    cat = Cat('Kitty', 3)
    dog = Dog('Fluffy', 4)
    for creature in (cat, dog):
        creature.info()
        creature.speak()

if __name__ == '__main__':
    main()