class Emp(object):
    org = "Bajaj" 
    def __init__(self, eid: str, ename: str, esal: float) -> None:
        self._eid = eid
        self._ename = ename
        self.__esal = esal

    @classmethod
    def modify(cls, n: str) -> None:
        cls.org = n

    @staticmethod
    def static_demo(n: str) -> None:
        Emp.org = n

    def display(self) -> None:
        print("EID\tEname\tEsal")
        print(f"{self._eid}\t{self._ename}\t{self.__esal}")

def main():
    ob = Emp("E001", "Kapil", 50000.00)
    ob.display()
    Emp.modify("GNU")
    print(Emp.org)
    ob.modify("Cisco")
    print(Emp.org)
    Emp.static_demo("Nike")
    print(Emp.org)
    ob.static_demo("JetBrains")
    print(Emp.org)

if __name__ == '__main__':
    main()