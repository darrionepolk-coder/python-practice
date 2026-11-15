# This program helps a student calculate their final course grade.
# It checks that each score is valid before doing any math.
# This is important because each class category has a different max score.

# These are the maximum points for each category in the course.
QUIZ_MAX = 40
MIDTERM_MAX = 25
FINAL_MAX = 35

# These numbers tell us how much each category counts toward the final grade.
# For example, the quiz is worth 40% of the total class grade.
QUIZ_WEIGHT = 0.40
MIDTERM_WEIGHT = 0.25
FINAL_WEIGHT = 0.35

# Step 1: ask the student for each score.
quiz = float(input(f"Enter quiz score (0 - {QUIZ_MAX}): "))
midterm = float(input(f"Enter midterm score (0 - {MIDTERM_MAX}): "))
final_exam = float(input(f"Enter final exam score (0 - {FINAL_MAX}): "))

# Step 2: validate the inputs before doing any final grade calculation.
# If a score is below 0 or above the category max, it is not valid.
if quiz < 0 or quiz > QUIZ_MAX:
    print(f"Invalid quiz score. Please enter a value between 0 and {QUIZ_MAX}.")
elif midterm < 0 or midterm > MIDTERM_MAX:
    print(f"Invalid midterm score. Please enter a value between 0 and {MIDTERM_MAX}.")
elif final_exam < 0 or final_exam > FINAL_MAX:
    print(f"Invalid final exam score. Please enter a value between 0 and {FINAL_MAX}.")
else:
    # Step 3: turn each category score into a percentage of that category's max.
    # Then multiply it by the category's weight to get its contribution.
    final_grade = ((quiz / QUIZ_MAX) * 100 * QUIZ_WEIGHT) + \
                  ((midterm / MIDTERM_MAX) * 100 * MIDTERM_WEIGHT) + \
                  ((final_exam / FINAL_MAX) * 100 * FINAL_WEIGHT)

    # Step 4: make sure the final grade never goes above 100% or below 0%.
    final_grade = min(max(final_grade, 0), 100)

    # Step 5: print the final result.
    print(f"Final grade: {final_grade:.2f}%")
