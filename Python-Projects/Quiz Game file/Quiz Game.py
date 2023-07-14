# Quiz Game

import csv

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer
    
    def display_question(self):
        print(self.question)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")
    
    def check_answer(self, user_answer):
        return user_answer == self.answer


def load_questions_from_csv(file_path):
    questions = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            question = row[0]
            options = row[1:5]
            answer = int(row[5])
            questions.append(Question(question, options, answer))
    return questions


def run_quiz(questions):
    score = 0
    for question in questions:
        print()
        question.display_question()
        user_answer = input("Your answer (enter the option number): ")
        if question.check_answer(int(user_answer)):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        print("-------------------")
    
    print("Quiz completed!")
    print(f"Your score: {score}/{len(questions)}")


# Load questions from CSV file
questions = load_questions_from_csv('questions.csv')

# Run the quiz
run_quiz(questions)


'''
=================================
Test Case:
=================================

What is the capital of France?
1. London
2. Paris
3. Berlin
4. Rome
Your answer (enter the option number): 1
Incorrect!
-------------------

Who painted the Mona Lisa?
1. Leonardo da Vinci
2. Pablo Picasso
3. Vincent van Gogh
4. Michelangelo
Your answer (enter the option number): 2
Incorrect!
-------------------

What is the largest planet in our solar system?
1. Mars
2. Jupiter
3. Venus
4. Saturn
Your answer (enter the option number): 2
Correct!
-------------------
Quiz completed!
Your score: 1/3

'''