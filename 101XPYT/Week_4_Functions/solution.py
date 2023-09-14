def get_student_details():
    name = input("Enter student name: ")
    return name

def get_scores():
    math_score = float(input("Enter Math score: "))
    english_score = float(input("Enter English score: "))
    science_score = float(input("Enter Science score: "))
    return math_score, english_score, science_score

def calculate_average(score1, score2, score3):
    total_score = score1 + score2 + score3
    average_score = total_score / 3
    return average_score

# Main program
print("Student Grade Calculator\n")

# Get student details
student_name = get_student_details()

# Get scores for Math, English, and Science
math_score, english_score, science_score = get_scores()

# Calculate average score
average_score = calculate_average(math_score, english_score, science_score)

# Determine grade
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
else:
    grade = "F"

# Print results
print("\nStudent Name:", student_name)
print("Average Score:", average_score)
print("Grade:", grade)
