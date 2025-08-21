import csv

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def input_marks(self, subjects):
        for subject in subjects:
            while True:
                try:
                    marks = int(input(f"Enter marks for {subject}: "))
                    if marks < 0 or marks > 100:
                        raise ValueError("Marks must be between 0 and 100")
                except ValueError as e:
                    print(f"Invalid input: {e}. Please try again.")
                    continue

                # Retest loop
                while marks < 40:
                    print(f"{self.name} failed in {subject}. Retest allowed.")  
                    marks = int(input(f"Enter marks for {subject} (retest): "))
                    if marks >= 40:
                        print(f"{self.name} passed in {subject} after retest.")
                        break

                self.grades[subject] = self.assign_grade(marks)
                break
    
    def assign_grade(self, marks):
        if marks >= 90:
            return 'A'
        elif marks >= 75:
            return 'B'
        elif marks >= 60:
            return 'C'
        elif marks >= 40:
            return 'D'
        else:
            return 'F'
        
    def grade_generation(self):
        """Generator to yield subject-wise grades"""
        for subject, grade in self.grades.items():
            yield subject, grade

def save_to_csv(student, subjects, filename="grades.csv"):
    """Save all subjects in one row per student"""
    file_exists = False
    try:
        with open(filename, "r"):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        # Write header only once
        if not file_exists:
            writer.writerow(["Name"] + subjects)
        
        row = [student.name] + [student.grades.get(sub, "NA") for sub in subjects]
        writer.writerow(row)

if __name__ == "__main__":
    subjects = ['Math', 'Science', 'English']
    num_students = int(input("Enter number of students: "))

    for _ in range(num_students):
        student_name = input("\nEnter the student name: ")
        student = Student(student_name)
        student.input_marks(subjects)

        print(f"\nGrades for {student.name}:")
        for subject, grade in student.grade_generation():
            print(f"{subject}: {grade}")

        save_to_csv(student, subjects)
        print(f"Grades saved to grades.csv")
