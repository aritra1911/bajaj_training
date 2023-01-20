from typing import Tuple

class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_student_info(self) -> Tuple[str, int]:
        return self.name, self.age

    def set_student_info(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

class ScienceStudent(Student):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    def get_job(self) -> str:
        return "Science"

def main():
    s = ScienceStudent("Ramesh", 30)
    print(s.get_student_info())
    s.set_student_info("Rahul", 35)
    print(s.get_student_info())
    print(s.get_job())

if __name__ == '__main__':
    main()