import random


def main():
    # State names are the keys and capital cities are the values.
    states = {
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Michigan": "Lansing",
        "Wisconsin": "Madison",
        "Ohio": "Columbus",
        "California": "Sacramento",
        "Texas": "Austin",
        "Florida": "Tallahassee",
        "New York": "Albany",
        "Colorado": "Denver",
        "Georgia": "Atlanta",
        "Oregon": "Salem",
        "Arizona": "Phoenix",
        "Nevada": "Carson City",
        "Missouri": "Jefferson City"
    }

    correct = 0
    incorrect = 0

    print("U.S. State Capital Game")
    print("Enter the capital of the selected state.")
    print("Type Q to quit.\n")

    while True:
        state = random.choice(list(states.keys()))
        answer = input("What is the capital of " + state + "? ")

        if answer.lower() == "q":
            break
        elif answer.strip().lower() == states[state].lower():
            print("Correct!\n")
            correct += 1
        else:
            print("Incorrect. The capital of " + state + " is "
                  + states[state] + ".\n")
            incorrect += 1

    total = correct + incorrect
    print("\nGame Summary")
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)
    print("Total questions answered:", total)

    if total > 0:
        percentage = correct / total * 100
        print("Correct percentage: {:.1f}%".format(percentage))
    else:
        print("You did not answer any questions.")


if __name__ == "__main__":
    main()
