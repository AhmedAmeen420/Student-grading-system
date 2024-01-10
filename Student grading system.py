def calculate_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 0 <= score <= 59:
        return 'F'
    else:
        return 'Invalid Score'

def student_grading_system():
    while True:
        score = input("Enter the score (or 'exit' to quit): ")

        if score.lower() == 'exit':
            print("Exiting the grading system. Goodbye!")
            break

        score = float(score)
        grade = calculate_grade(score)
        print("Grade:", grade)

# Run the student grading system
student_grading_system()

