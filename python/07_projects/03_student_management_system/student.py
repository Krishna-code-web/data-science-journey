import json
import os


class Student:
    def __init__(self, student_id, name, age, branch, tenth_marks, twelfth_marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.branch = branch
        self.tenth_marks = tenth_marks
        self.twelfth_marks = twelfth_marks

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "branch": self.branch,
            "tenth_marks": self.tenth_marks,
            "twelfth_marks": self.twelfth_marks
        }


class StudentManagement:
    def __init__(self):
        self.file_name = "students.json"
        self.students = []
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.file_name):
            return

        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)

                for student_data in data:
                    student = Student(
                        student_data["student_id"],
                        student_data["name"],
                        student_data["age"],
                        student_data["branch"],
                        student_data["tenth_marks"],
                        student_data["twelfth_marks"]
                    )

                    self.students.append(student)

        except json.JSONDecodeError:
            self.students = []

    def save_data(self):
        data = []

        for student in self.students:
            data.append(student.to_dict())

        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def add_student(self):
        try:
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            branch = input("Enter Branch: ")
            tenth_marks = float(input("Enter 10th Marks: "))
            twelfth_marks = float(input("Enter 12th Marks: "))

            for student in self.students:
                if student.student_id == student_id:
                    print("Student ID already exists!")
                    return

            student = Student(
                student_id,
                name,
                age,
                branch,
                tenth_marks,
                twelfth_marks
            )

            self.students.append(student)
            self.save_data()

            print("Student added successfully!")

        except ValueError:
            print("Invalid input!")

    def view_students(self):
        if not self.students:
            print("No students found!")
            return

        print("\n")
        print("-" * 80)

        for student in self.students:
            print(
                f"ID: {student.student_id} | "
                f"Name: {student.name} | "
                f"Age: {student.age} | "
                f"Branch: {student.branch} | "
                f"10th: {student.tenth_marks} | "
                f"12th: {student.twelfth_marks}"
            )

        print("-" * 80)

    def search_student(self):
        try:
            student_id = int(input("Enter Student ID: "))

            for student in self.students:
                if student.student_id == student_id:
                    print("\nStudent Found")
                    print(f"ID: {student.student_id}")
                    print(f"Name: {student.name}")
                    print(f"Age: {student.age}")
                    print(f"Branch: {student.branch}")
                    print(f"10th Marks: {student.tenth_marks}")
                    print(f"12th Marks: {student.twelfth_marks}")
                    return

            print("Student not found!")

        except ValueError:
            print("Invalid ID!")

    def update_student(self):
        try:
            student_id = int(input("Enter Student ID to update: "))

            for student in self.students:
                if student.student_id == student_id:

                    student.name = input("Enter New Name: ")
                    student.age = int(input("Enter New Age: "))
                    student.branch = input("Enter New Branch: ")
                    student.tenth_marks = float(input("Enter New 10th Marks: "))
                    student.twelfth_marks = float(input("Enter New 12th Marks: "))

                    self.save_data()

                    print("Student updated successfully!")
                    return

            print("Student not found!")

        except ValueError:
            print("Invalid input!")

    def delete_student(self):
        try:
            student_id = int(input("Enter Student ID to delete: "))

            for student in self.students:
                if student.student_id == student_id:
                    self.students.remove(student)

                    self.save_data()

                    print("Student deleted successfully!")
                    return

            print("Student not found!")

        except ValueError:
            print("Invalid ID!")

    def topper(self):
        if not self.students:
            print("No students found!")
            return

        topper = max(
            self.students,
            key=lambda student: student.twelfth_marks
        )

        print("\nTopper Student")
        print(f"Name: {topper.name}")
        print(f"12th Marks: {topper.twelfth_marks}")

    def average_marks(self):
        if not self.students:
            print("No students found!")
            return

        avg = sum(
            student.twelfth_marks
            for student in self.students
        ) / len(self.students)

        print(f"\nAverage 12th Marks: {avg:.2f}")


def main():
    manager = StudentManagement()

    while True:
        print("\n")
        print("=" * 50)
        print("STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Topper")
        print("7. Average Marks")
        print("8. Exit")

        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                manager.add_student()

            elif choice == 2:
                manager.view_students()

            elif choice == 3:
                manager.search_student()

            elif choice == 4:
                manager.update_student()

            elif choice == 5:
                manager.delete_student()

            elif choice == 6:
                manager.topper()

            elif choice == 7:
                manager.average_marks()

            elif choice == 8:
                print("Goodbye!")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number!")


if __name__ == "__main__":
    main()