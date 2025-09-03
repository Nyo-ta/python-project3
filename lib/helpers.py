from models import session, Student, Task

def create_student():
    name = input("Student name: ")
    student = Student(name=name)
    session.add(student)
    session.commit()
    print("Student added")

def create_task():
    description = input("Task description: ")
    student_id = int(input("Student ID: "))
    student = session.get(Student, student_id)
    if student:
        task = Task(description=description, student=student)
        session.add(task)
        session.commit()
        print("Task added")
    else:
        print("Student not found")

def list_students():
    for student in session.query(Student).all():
        print(student)

def show_student_tasks():
    student_id = int(input("Student ID: "))
    student = session.get(Student, student_id)
    if student:
        print(student)
        for task in student.tasks:
            print(task)
    else:
        print("Student not found")

def exit_program():
    exit()


