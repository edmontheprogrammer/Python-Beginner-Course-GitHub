# Write a program that rolls a dice with two values such as (3, 4) and
# (0, 2) using Random 
# 1. Create a class named Dice
# 2. Define a roll() method with tuple list, read only list
# 

import random
class Dice:
    def roll(self):
        dice_values = 0, 1, 2, 3, 4, 5, 6
        number_1 = random.choice(dice_values)
        number_2 = random.choice(dice_values)
        print(f'({number_1},{number_2})')


dice = Dice()
roll_once = dice.roll()
roll_second = dice.roll()
