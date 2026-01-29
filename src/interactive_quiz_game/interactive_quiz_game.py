"""
Interactive Quiz Game 
by. Akhila Chitluri
Description: A general knowledge quiz game using input, output,
decisions, and loops.
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
    print("----------------------------------------")
    print("🎯 Welcome to the Interactive Quiz Game!")
    print("Test your general knowledge and see how you score.\n")

    user_name = input("Please enter your name: ").strip()

    questions = [
        "1) What is the capital of France?\nA) Paris\nB) Rome\nC) Madrid\nD) Berlin",
        "2) Which layer of Earth lies directly beneath the crust?\nA) Inner core\nB) Outer core\nC) Lithosphere\nD) Mantle",
        "3) Which country has the longest coastline in the world?\nA) United States\nB) Australia\nC) Canada\nD) Russia",
        "4) Which data type stores whole numbers in Python?\nA) float\nB) string\nC) int\nD) boolean",
        "5) What is the smallest prime number greater than 50?\nA) 51\nB) 53\nC) 57\nD) 59",
    ]

    answers = ["a", "d", "c", "c", "b"]

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