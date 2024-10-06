def student_enrollment_system():
    courses = {}

    print("\nStudent Enrollment System")
    print("1. Enroll Student")
    print("2. View Enrolled Students")
    print("3. Remove Student")
    print("4. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            std_name = input("Enter the student name: ")
            course = input("Enter the couse name: ")

            if course not in courses:
                courses[course] = set()
            
            courses[course].add(std_name)
            print(f"{std_name} has been enrolled to the course {course}.")

        elif choice == '2':
            course = input("Enter the course name: ")

            if course in courses:
                print(f"Students enrolled in {course}: {courses[course]}")
            else:
                print(f"No students enrolled in {course}.")

        elif choice == '3':
            std_name = input("Enter student name: ")
            course = input("Enter the course name: ")

            if course in courses and std_name in courses[course]:
                courses[course].remove(std_name)
                print(f"The student {std_name} has been removed from {course}.")
            else:
                print(f"No student found in {course}.")

        elif choice == '4':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice")

student_enrollment_system()