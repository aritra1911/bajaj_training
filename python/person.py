from typing import Optional

class Person:
    def __init__(self, name: str, job: Optional[str]=None, pay: int=0):
        self.name = name
        self.job = job
        self.pay = pay

    def __repr__(self) -> str:
        return "[Person %s, %s, %s]" % (self.name, self.job, self.pay)

    def __str__(self) -> str:
        return "%s, job='%s', pay='%s'" % (self.name, self.job, self.pay)

    def get_last_name(self) -> str:
        return self.name.split(' ')[-1]

    def give_raise(self, percent: float) -> None:
        self.pay = int(self.pay * (1 + percent / 100.))

def main():
    bob = Person("Bob Smith")
    sue = Person("Sue Jonas", job="dev", pay=100000)
    bob.give_raise(20)
    print(bob.get_last_name(), "pay =", bob.pay)

if __name__ == '__main__':
    main()