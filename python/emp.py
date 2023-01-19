class Emp:
    def __init__(self, eid: str, ename: str, esal: float) -> None:
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def display(self):
        print("EID\tEname\tEsal")
        print(f"{self.eid}\t{self.ename}\t{self.esal}")

def main():
    ob = Emp("E001", "Kapil", 50000.00)
    ob.display()

if __name__ == '__main__':
    main()