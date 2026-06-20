import json
import os


class Book:
    def __init__(self, book_id, title, author, copies_available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies_available = copies_available

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "copies_available": self.copies_available
        }


class Student:
    def __init__(self, student_id, name, branch, issued_books=None):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.issued_books = issued_books if issued_books else []

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "branch": self.branch,
            "issued_books": self.issued_books
        }


class Library:
    def __init__(self):
        self.books = []
        self.students = []

        self.load_books()
        self.load_students()

    # --------------------------
    # Helper Methods
    # --------------------------

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    # --------------------------
    # Book Operations
    # --------------------------

    def add_book(self):
        try:
            book_id = int(input("Book ID: "))

            if self.find_book(book_id):
                print("Book already exists!")
                return

            title = input("Title: ")
            author = input("Author: ")
            copies = int(input("Copies Available: "))

            book = Book(book_id, title, author, copies)

            self.books.append(book)

            self.save_books()

            print("Book added successfully!")

        except ValueError:
            print("Invalid input!")

    def view_books(self):
        if not self.books:
            print("\nNo books available!")
            return

        print("\n")
        print("=" * 90)
        print(
            f"{'BOOK ID':<10}"
            f"{'TITLE':<35}"
            f"{'AUTHOR':<25}"
            f"{'COPIES':<10}"
        )
        print("=" * 90)

        for book in self.books:
            print(
                f"{book.book_id:<10}"
                f"{book.title:<35}"
                f"{book.author:<25}"
                f"{book.copies_available:<10}"
            )

        print("=" * 90)

    def search_book(self):
        try:
            book_id = int(input("Enter Book ID: "))

            book = self.find_book(book_id)

            if not book:
                print("Book not found!")
                return

            print("\nBook Details")
            print("-" * 40)
            print(f"Book ID           : {book.book_id}")
            print(f"Title             : {book.title}")
            print(f"Author            : {book.author}")
            print(f"Copies Available  : {book.copies_available}")

        except ValueError:
            print("Invalid ID!")

    def remove_book(self):
        try:
            book_id = int(input("Enter Book ID: "))

            book = self.find_book(book_id)

            if not book:
                print("Book not found!")
                return

            self.books.remove(book)

            self.save_books()

            print("Book removed successfully!")

        except ValueError:
            print("Invalid ID!")

    # --------------------------
    # Student Operations
    # --------------------------

    def register_student(self):
        try:
            student_id = int(input("Student ID: "))

            if self.find_student(student_id):
                print("Student already exists!")
                return

            name = input("Name: ")
            branch = input("Branch: ")

            student = Student(student_id, name, branch)

            self.students.append(student)

            self.save_students()

            print("Student registered successfully!")

        except ValueError:
            print("Invalid input!")

    def view_students(self):
        if not self.students:
            print("\nNo students registered!")
            return

        print("\n")
        print("=" * 100)
        print(
            f"{'STUDENT ID':<15}"
            f"{'NAME':<30}"
            f"{'BRANCH':<20}"
            f"{'ISSUED BOOKS'}"
        )
        print("=" * 100)

        for student in self.students:

            issued = (
                ", ".join(map(str, student.issued_books))
                if student.issued_books
                else "None"
            )

            print(
                f"{student.student_id:<15}"
                f"{student.name:<30}"
                f"{student.branch:<20}"
                f"{issued}"
            )

        print("=" * 100)

    def search_student(self):
        try:
            student_id = int(input("Enter Student ID: "))

            student = self.find_student(student_id)

            if not student:
                print("Student not found!")
                return

            print("\nStudent Details")
            print("-" * 40)

            print(f"Student ID : {student.student_id}")
            print(f"Name       : {student.name}")
            print(f"Branch     : {student.branch}")

            if student.issued_books:
                print(
                    f"Issued Books : "
                    f"{', '.join(map(str, student.issued_books))}"
                )
            else:
                print("Issued Books : None")

        except ValueError:
            print("Invalid ID!")

    def remove_student(self):
        try:
            student_id = int(input("Enter Student ID: "))

            student = self.find_student(student_id)

            if not student:
                print("Student not found!")
                return

            self.students.remove(student)

            self.save_students()

            print("Student removed successfully!")

        except ValueError:
            print("Invalid ID!")

    # --------------------------
    # Issue / Return
    # --------------------------

    def issue_book(self):
        try:
            student_id = int(input("Student ID: "))
            book_id = int(input("Book ID: "))

            student = self.find_student(student_id)
            book = self.find_book(book_id)

            if not student:
                print("Student not found!")
                return

            if not book:
                print("Book not found!")
                return

            if book.copies_available <= 0:
                print("Book unavailable!")
                return

            if book_id in student.issued_books:
                print("Book already issued!")
                return

            student.issued_books.append(book_id)

            book.copies_available -= 1

            self.save_books()
            self.save_students()

            print("Book issued successfully!")

        except ValueError:
            print("Invalid input!")

    def return_book(self):
        try:
            student_id = int(input("Student ID: "))
            book_id = int(input("Book ID: "))

            student = self.find_student(student_id)
            book = self.find_book(book_id)

            if not student:
                print("Student not found!")
                return

            if not book:
                print("Book not found!")
                return

            if book_id not in student.issued_books:
                print("This book was not issued!")
                return

            student.issued_books.remove(book_id)

            book.copies_available += 1

            self.save_books()
            self.save_students()

            print("Book returned successfully!")

        except ValueError:
            print("Invalid input!")

    # --------------------------
    # Save / Load
    # --------------------------

    def save_books(self):
        data = [book.to_dict() for book in self.books]

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

    def save_students(self):
        data = [student.to_dict() for student in self.students]

        with open("students.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_books(self):
        if not os.path.exists("books.json"):
            return

        try:
            with open("books.json", "r") as file:
                data = json.load(file)

                self.books = [
                    Book(
                        book["book_id"],
                        book["title"],
                        book["author"],
                        book["copies_available"]
                    )
                    for book in data
                ]

        except json.JSONDecodeError:
            self.books = []

    def load_students(self):
        if not os.path.exists("students.json"):
            return

        try:
            with open("students.json", "r") as file:
                data = json.load(file)

                self.students = [
                    Student(
                        student["student_id"],
                        student["name"],
                        student["branch"],
                        student["issued_books"]
                    )
                    for student in data
                ]

        except json.JSONDecodeError:
            self.students = []
    
    def display_menu(self):
        print("\n" + "=" * 60)
        print("           LIBRARY MANAGEMENT SYSTEM")
        print("=" * 60)

        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")

        print("\n5. Register Student")
        print("6. View Students")
        print("7. Search Student")
        print("8. Remove Student")

        print("\n9. Issue Book")
        print("10. Return Book")

        print("\n11. Exit")

        print("=" * 60)

    def run(self):

        while True:

            self.display_menu()

            try:
                choice = int(input("\nEnter Choice: "))

                if choice == 1:
                    self.add_book()

                elif choice == 2:
                    self.view_books()

                elif choice == 3:
                    self.search_book()

                elif choice == 4:
                    self.remove_book()

                elif choice == 5:
                    self.register_student()

                elif choice == 6:
                    self.view_students()

                elif choice == 7:
                    self.search_student()

                elif choice == 8:
                    self.remove_student()

                elif choice == 9:
                    self.issue_book()

                elif choice == 10:
                    self.return_book()

                elif choice == 11:
                    print("\nThank you for using Library Management System!")
                    break

                else:
                    print("Invalid Choice!")

            except ValueError:
                print("Please enter a valid number!")
    
if __name__ == "__main__":
    library = Library()
    library.run()