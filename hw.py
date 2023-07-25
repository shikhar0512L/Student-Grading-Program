def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif 80 <= marks < 90:
        return 'A'
    elif 70 <= marks < 80:
        return 'B'
    elif 60 <= marks < 70:
        return 'C'
    elif 50 <= marks < 60:
        return 'D'
    else:
        return 'Fail'

def main():
    while True:
        try:
            marks = int(input("Enter the marks obtained by the student: "))
            if marks < 0 or marks > 100:
                print("Invalid marks! Please enter marks between 0 and 100.")
                continue

            grade = calculate_grade(marks)
            print("Grade: ", grade)

            another_student = input("Do you want to calculate the grade for another student? (yes/no): ")
            if another_student.lower() == 'no':
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
