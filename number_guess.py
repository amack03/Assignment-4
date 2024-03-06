'''This is a game where the player is suppost to guess a number 1-10. If the user correctly guesses the random number they win. If they guess incorrectly they are asked to try again and again until they guess correctly'''

import random

number = random.randrange(1,10)
count = 0
guess = 0

while guess != number:
    guess = int(input("Enter a number 1-10: "))

    count += 1
    
    if number != guess:
        print(f"Incorrect, you guessed {guess}. Try again.")

print(f"Good job! You guessed {number} in {count} tries!")