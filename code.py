from abc import ABC
from abc import abstractmethod


class Student(ABC):
    def __init__(self, name, rollno):
        self._name=name
        self._rollno=rollno

    

    @property
    def name(self):
        return self._name

    @property
    def rollno(self):
        return self._rollno

    @abstractmethod
    def display_info(self):
     pass

class SchoolStudent(Student):
        def __init__(self, name, rollno, grade, section):
             super().__init__(name, rollno)
             self._grade=grade
             self._section=section

        def display_info(self):
             print(f"[School Student]---\n Name: {self.name} \n Roll No.: {self.rollno} \n Grade: {self._grade} \n Section: {self._section} ")

class CollegeStudent(Student):
        def __init__(self, name, rollno, year, branch):
             super().__init__(name, rollno)
             self._year=year
             self._branch=branch

        def display_info(self):
             print(f"[College Student]---\n Name: {self.name} \n Roll No.: {self.rollno} \n Year: {self._year} \n Branch: {self._branch}")

def create_school_student():
    name = input("Enter school student name:")
    rollno = input("Enter roll number:")
    grade = input("Enter Grade:")
    section = input("Enter Section:")
    return SchoolStudent(name, rollno, grade, section)


def create_college_student(): 
    name = input("Enter college student name: ")
    rollno = input("Enter roll number: ")
    year = input("Enter Year:")
    branch = input("Enter branch:")
    return CollegeStudent(name, rollno, year, branch)

def main():
    students = []

    n = int(input("No. of School students:"))
    for _ in range(n):
        students.append(create_school_student())

    n = int(input("No. of College students:"))
    for _ in range(n):
        students.append(create_college_student())

    print("\n--- Student Records ---")
    for s in students:
        s.display_info()

if __name__ == "__main__":
    main()