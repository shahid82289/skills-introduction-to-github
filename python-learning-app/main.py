"""Simple interactive Python learning app."""


def show_menu() -> None:
    print("\n=== Python Learning App ===")
    print("1. Learn: Variables")
    print("2. Learn: Loops")
    print("3. Quiz")
    print("4. Exit")


def lesson_variables() -> None:
    print("\nVariables store values in memory.")
    print("Example: name = 'Mona' and age = 5")


def lesson_loops() -> None:
    print("\nLoops repeat actions.")
    print("Example: for i in range(3): print(i)")


def quiz() -> None:
    questions = [
        (
            "Which keyword starts a loop over a sequence?",
            {"a": "if", "b": "for", "c": "def"},
            "b",
        ),
        (
            "What symbol is used for assignment in Python?",
            {"a": "=", "b": "==", "c": ":="},
            "a",
        ),
    ]

    score = 0
    print("\nQuiz time!")
    for index, (prompt, options, answer) in enumerate(questions, start=1):
        print(f"\nQ{index}. {prompt}")
        for key, value in options.items():
            print(f"  {key}) {value}")
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == answer:
            score += 1
            print("Correct!")
        else:
            print(f"Not quite. Correct answer: {answer}")

    print(f"\nYou scored {score}/{len(questions)}.")


def main() -> None:
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            lesson_variables()
        elif choice == "2":
            lesson_loops()
        elif choice == "3":
            quiz()
        elif choice == "4":
            print("Goodbye and keep learning Python!")
            break
        else:
            print("Please enter a valid option: 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
