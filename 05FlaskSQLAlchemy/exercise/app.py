from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from typing import List, Optional

app: Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']: str = 'sqlite:///students.db'
db: SQLAlchemy = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    age: int = db.Column(db.Integer, nullable=False)
    grade: str = db.Column(db.String(10), nullable=False)

    def __repr__(self) -> str:
        return f"<Student {self.name}>"

# Create the database and tables
with app.app_context():
    db.create_all()

# Helper functions for CRUD operations

def add_student(name: str, age: int, grade: str) -> Student:
    student: Student = Student(name=name, age=age, grade=grade)
    db.session.add(student)
    db.session.commit()
    return student

def get_student_by_id(id: int) -> Optional[Student]:
    return db.session.get(Student, id)

def get_all_students() -> List[Student]:
    return Student.query.all()

def update_student(id: int, name: str, age: int, grade: str) -> Optional[Student]:
    student: Optional[Student] = db.session.get(Student, id)
    if student:
        student.name = name
        student.age = age
        student.grade = grade
        db.session.commit()
    return student

def delete_student(id: int) -> None:
    student: Optional[Student] = db.session.get(Student, id)
    if student:
        db.session.delete(student)
        db.session.commit()

if __name__ == '__main__':
    # Sample usage of the functions:
    with app.app_context():
        # Add students
        student1: Student = add_student('John Doe', 22, 'A')
        student2: Student = add_student('Jane Smith', 20, 'B')

        # Get students by ID
        print(get_student_by_id(student1.id))
        print(get_student_by_id(student2.id))

        # Get all students
        all_students: List[Student] = get_all_students()
        for student in all_students:
            print(student)

        # Update student
        update_student(student1.id, 'John Doe Jr.', 23, 'A+')
        updated_student: Optional[Student] = get_student_by_id(student1.id)
        if updated_student:
            print(updated_student)

        # Delete student
        delete_student(student2.id)
