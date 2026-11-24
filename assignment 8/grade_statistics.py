
from pathlib import Path

GRADES_FILE = Path(__file__).resolve().parent / "grades.csv"

TEST_WEIGHT = 0.3
EXAM_WEIGHT = 0.3
DISCUSSION_WEIGHT = 0.2
PROJECT_WEIGHT = 0.2


def main():
    """Read the grades file, compute each student's weighted final
    grade, and print a summary of how many students fall into each
    grade range."""

    try:
        weighted_final_list = []

        with open(GRADES_FILE, 'r') as input_file:
            # Skip the header row.
            input_file.readline()

            # Read and process each student's grades.
            for line in input_file:
                if line.strip():
                    row = line.strip().split(',')
                    weighted_final_list.append(process_row(row))

        # Analyze the final grades.
        analyze_grade(weighted_final_list)

    except FileNotFoundError:
        print(f"Could not find the file: {GRADES_FILE}")

    except (OSError, ValueError, IndexError, ZeroDivisionError) as error:
        print(f"An error occurred while processing the grades: {error}")


def process_row(row):
    """Given one row from the grades file, return that student's
    weighted final grade (bypass the Name and StudentID columns)."""

    # Calculate the average for each category using list slicing.
    test_avg = average_subject(row[2:6])
    exam_avg = average_subject(row[6:8])
    discussion_avg = average_subject(row[8:10])

    # Get the project score.
    project_score = float(row[10])

    # Calculate and return the weighted final grade.
    return weight_final(
        test_avg,
        exam_avg,
        discussion_avg,
        project_score
    )


def average_subject(subject_list):
    """Return the average of the scores in subject_list."""

    total = 0

    for score in subject_list:
        total += float(score)

    return total / len(subject_list)


def weight_final(test_avg, exam_avg, discussion_avg, project_score):
    """Return a student's weighted final grade, combining the test,
    exam, discussion, and project scores using the weight constants
    declared above."""

    final_grade = (
        test_avg * TEST_WEIGHT
        + exam_avg * EXAM_WEIGHT
        + discussion_avg * DISCUSSION_WEIGHT
        + project_score * PROJECT_WEIGHT
    )

    return final_grade


def analyze_grade(weight_final_list):
    """Count and print how many students fall into each grade range:
    90 or above, 80-89, 70-79, 60-69, and below 60."""

    # Initialize grade counters.
    grade_90 = 0
    grade_80 = 0
    grade_70 = 0
    grade_60 = 0
    grade_below_60 = 0

    # Count students in each grade range.
    for grade in weight_final_list:
        if grade >= 90:
            grade_90 += 1
        elif grade >= 80:
            grade_80 += 1
        elif grade >= 70:
            grade_70 += 1
        elif grade >= 60:
            grade_60 += 1
        else:
            grade_below_60 += 1

    # Display the results.
    print("\nGrade Statistics")
    print("-------------------------")
    print(f"90 and above: {grade_90}")
    print(f"80-89: {grade_80}")
    print(f"70-79: {grade_70}")
    print(f"60-69: {grade_60}")
    print(f"Below 60: {grade_below_60}")


if __name__ == "__main__":
    main()
