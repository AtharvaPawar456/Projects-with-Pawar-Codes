# Unit Conversion Quiz

import random

# Dictionary of conversion factors for different units
conversion_factors = {
    "cm to inch": 0.393701,
    "inch to cm": 2.54,
    "m to ft": 3.28084,
    "ft to m": 0.3048,
    "km to mile": 0.621371,
    "mile to km": 1.60934
}

def generate_quiz_question():
    # Randomly select a conversion factor from the dictionary
    conversion = random.choice(list(conversion_factors.keys()))
    factor = conversion_factors[conversion]

    # Generate a random number for the conversion question
    value = random.randint(1, 100)

    # Calculate the expected answer
    expected_answer = value * factor

    # Format the question
    question = f"Convert {value} {conversion.split(' to ')[0]} to {conversion.split(' to ')[1]}: "

    return question, expected_answer

def check_answer(question, expected_answer, user_answer):
    # Check if the user's answer matches the expected answer
    if abs(user_answer - expected_answer) < 0.0001:
        return True
    else:
        return False

# Main program
score = 0
num_questions = 5

print("Unit Conversion Quiz")
print("Answer the following questions:")

for _ in range(num_questions):
    question, expected_answer = generate_quiz_question()
    user_answer = float(input(question))
    if check_answer(question, expected_answer, user_answer):
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {expected_answer}")

print(f"Quiz complete! Your score: {score}/{num_questions}")


'''
=================================
Test Case:
=================================

Unit Conversion Quiz
Answer the following questions:
Convert 62 ft to m: 23
Wrong! The correct answer is 18.8976
Convert 92 mile to km: 34
Wrong! The correct answer is 148.05928
Convert 72 km to mile: 23
Wrong! The correct answer is 44.738712
Convert 23 km to mile: 32
Wrong! The correct answer is 14.291533


'''