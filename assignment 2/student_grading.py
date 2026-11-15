# Define the weight of each category in the final grade
QUIZ_WEIGHT = 0.40
MIDTERM_WEIGHT = 0.25
FINAL_WEIGHT = 0.35

# Input: get the student's percentage scores for each category
quiz = float(input("Enter quiz grade (%): "))
midterm = float(input("Enter midterm grade (%): "))
final_exam = float(input("Enter final exam grade (%): "))

# Process: calculate the weighted final grade using percentage values
final_grade = (quiz * QUIZ_WEIGHT) + (midterm * MIDTERM_WEIGHT) + (final_exam * FINAL_WEIGHT)

# Keep the final grade within the 0% to 100% range
final_grade = min(max(final_grade, 0), 100)

# Output: display the final grade as a percentage with 2 decimal places
print(f"Final grade: {final_grade:.2f}%")
