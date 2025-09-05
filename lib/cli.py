from helpers import (
    create_student,
    create_task,
    list_students,
    show_student_tasks,
    exit_program,
)


def menu():
    print("1. Add student")
    print("2. Add task")
    print("3. List students")
    print("4. Show student tasks")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            create_student()
        elif choice == "2":
            create_task()
        elif choice == "3":
            list_students()
        elif choice == "4":
            show_student_tasks()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid")

if __name__ == "__main__":
    main()


