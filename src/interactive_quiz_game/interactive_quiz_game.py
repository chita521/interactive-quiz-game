"""
Interactive Quiz Game 
by. Akhila Chitluri 
"""
def run_quiz(questions, answers):
    """
    Runs the quiz by looping through each question,
    collecting user input, and checking answers.
    """
    score = 0

    for index in range(len(questions)):
        print("\n" + questions[index])
        user_answer = input("Your answer (A, B, C, or D): ").strip().lower()

        if user_answer == answers[index]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {answers[index].upper()}.")

    return score


def main():
    print("🎯 Welcome to the Interactive Quiz Game!")
    print("Test your general knowledge and see how you score.\n")

    user_name = input("Please enter your name: ").strip()

    questions = [
        "1) What is the capital of France?\nA) Paris\nB) Rome\nC) Madrid\nD) Berlin",
        "2) Which planet is known as the Red Planet?\nA) Earth\nB) Mars\nC) Jupiter\nD) Venus",
        "3) What is the largest ocean on Earth?\nA) Atlantic\nB) Indian\nC) Arctic\nD) Pacific",
        "4) Which data type stores whole numbers in Python?\nA) float\nB) string\nC) int\nD) boolean",
        "5) Which keyword is used to repeat code while a condition is true?\nA) if\nB) for\nC) while\nD) repeat"
    ]

    answers = ["a", "b", "d", "c", "c"]

    play_again = "yes"

    while play_again == "yes":
        print(f"\nGood luck, {user_name}! Let's begin the quiz.")
        score = run_quiz(questions, answers)

        print("\n📊 Quiz Complete!")
        print(f"Final Score: {score} out of {len(questions)}")

        if score == len(questions):
            print("🏆 Perfect score! Excellent work!")
        elif score >= 3:
            print("👍 Nice job! You have strong general knowledge.")
        else:
            print("📘 Keep practicing — you'll improve with time.")

        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()

    print("\nThanks for playing! 👋 Have a great day.")

if __name__ == "__main__":
    main()
