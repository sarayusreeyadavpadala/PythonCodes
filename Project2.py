class Person:
    def __init__(self, name):
        self.__name = name  

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

class Student(Person):
    def __init__(self, name, roll_no, branch):
        super().__init__(name) 
        self.__roll_no = roll_no
        self.__branch = branch

    def get_roll_no(self):
        return self.__roll_no

    def get_branch(self):
        return self.__branch

    def set_marks(self, branch):
        self.__branch = branch

   
    def __str__(self):
        return f"Student: {self.get_name()}, Roll No: {self.__roll_no}, Branch: {self.__branch}"


class PGStudent(Student):
    def __init__(self, name, roll_no,branch, thesis_topic):
        super().__init__(name, roll_no, branch)
        self.thesis_topic = thesis_topic

    def __str__(self):
        return f"PGrad Student: {self.get_name()}, Roll No: {self.get_roll_no()}, Branch: {self.get_branch()}, Thesis: {self.thesis_topic}"


class StudentManager:
    def __init__(self):
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def get_all_students(self):
        return self.__students

    def find_by_roll(self, roll_no):
        for s in self.__students:
            if s.get_roll_no() == roll_no:
                return s
        return None


class App:
    def __init__(self):
        self.manager = StudentManager()

    def run(self):
        while True:
            print("\n===== Student Management System =====")
            print("1. Add Student")
            print("2. Add PostGraduate Student")
            print("3. View All Students")
            print("4. Search Student by Roll No")
            print("5. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_Pgraduate_student()
            elif choice == '3':
                self.show_all_students()
            elif choice == '4':
                self.search_student()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")

    def add_student(self):
        name = input("Enter name: ")
        roll_no = input("Enter roll no: ")
        branch = input("Enter branch: ")
        student = Student(name, roll_no, branch)
        self.manager.add_student(student)
        print("Student added.")

    def add_Pgraduate_student(self):
        name = input("Enter name: ")
        roll_no = input("Enter roll no: ")
        branch = input("Enter branch: ")
        thesis = input("Enter thesis topic: ")
        grad_student = PGStudent(name, roll_no, branch, thesis)
        self.manager.add_student(grad_student)
        print("Graduate student added.")

    def show_all_students(self):
        students = self.manager.get_all_students()
        if not students:
            print("No students found.")
        for s in students:
            print(s)

    def search_student(self):
        roll_no = input("Enter roll no to search: ")
        student = self.manager.find_by_roll(roll_no)
        if student:
            print("Found:", student)
        else:
            print("Student not found.")


if __name__ == "__main__":
    app = App()
    app.run()