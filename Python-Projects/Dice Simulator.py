# Dice Simulator 

import random

def roll_dice():
    return random.randint(1, 6)

# Test the dice simulator
num_rolls = int(input("Enter the number of times to roll the dice: "))

print("Dice rolls:")
for _ in range(num_rolls):
    dice_roll = roll_dice()
    print(dice_roll)


'''
=================================
Test Case:
=================================

Enter the number of times to roll the dice: 4
Dice rolls:
6
6
6
2

'''