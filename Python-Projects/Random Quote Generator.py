# Random Quote Generator

import random

def generate_random_quote():
    quotes = [
        "Be yourself; everyone else is already taken. - Oscar Wilde",
        "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. - Albert Einstein",
        "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Believe you can and you're halfway there. - Theodore Roosevelt"
    ]

    return random.choice(quotes)

# Test the random quote generator
random_quote = generate_random_quote()
print("Random Quote:")
print(random_quote)


'''
=================================
Test Case:
=================================

Random Quote:
Believe you can and you're halfway there. - Theodore Roosevelt

'''