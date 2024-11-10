import random

def _rndm_number(min_value, max_value):
    """Generate a random integer between min_value and max_value."""
    return random.randint(min_value, max_value)

def _random_operator():
    ""Randomly select an arithmetic operator from +, -, and *.""
    return random.choice(['+', '-', '*'])

def _math_problem(num1, num2, operator):
    """Create a math problem string and calculate the correct answer.

    Parameters:
        num1 (int): The first number in the problem.
        num2 (int): The second number in the problem.
        operator (str): The operator to use in the problem.

    Return:
        tuple: A string representing the math problem and the correct answer.
    """
    problem_text = f"{num1} {operator} {num2}"
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    return problem_text, correct_answer

def math_quiz():
    """Run a math quiz game where the user answers randomly generated math problems."""
    score = 0
    total_questions = 3  # Number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and operator for the math problem
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 5)
        operator = choose_random_operator()

        # Create the math problem and get the correct answer
        problem_text, correct_answer = create_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem_text}")

        # Try to get a valid integer input from the user
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        # Check if the user's answer is correct and update the score
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
