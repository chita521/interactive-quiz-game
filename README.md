# interactive-quiz-game

## Overview
The Interactive Quiz Game is a Python program designed to make learning and review more engaging by turning general knowledge and basic programming concepts into an interactive quiz experience. This program is intended for students or users who want a simple, user-friendly way to test their knowledge while demonstrating core programming structures.

## How to Run the Program
1. Ensure Python is installed on your computer.
2. Open the project folder in VS Code.
3. Run the file named `main.py`. 

## How the Program Works
- The program asks the user to enter their name.
- The user is presented with five multiple-choice general knowledge questions.
- The user enters their answer for each question.
- The program checks each answer and provides immediate feedback.
- A final score is displayed at the end of the quiz.
- The user is given the option to replay the quiz or exit the program.

## User Inputs
- User name (text input)
- Quiz answers (A, B, C, or D)
- Replay choice (yes or no)

## Programming Structures Used
- **Input:** User name, quiz answers, replay choice
- **Output:** Questions, feedback messages, final score, replay messages
- **Decisions:** IF / ELIF / ELSE statements to check answers and provide feedback
- **Loops:** 
  - FOR loop to iterate through quiz questions
  - WHILE loop to allow the user to replay the quiz

## Data Types Used
- `string` (user input, answers)
- `integer` (score tracking)
- `list` (questions and correct answers)

## Changes from Initial Plan
The original plan included fewer questions. The project was expanded to include five general knowledge questions to improve user engagement and better demonstrate looping and decision-making structures while keeping the program simple and clear.

## Project Tools and Workflow
- Python programming language
- Poetry used for project management (`pyproject.toml`)
- GitHub used for version control with multiple descriptive commits

## Notes for the User
The program is designed to be easy to use, clearly labeled, and understandable without the creator present. All instructions and prompts are provided within the program and this README file.
