#Tyler Harrison period 8

from ArtCode import random_colors
from Presets import preset_colors

#asks the user if they want random or set colors
print("Do you want the preset colors or randomized colors?: ")
correct_answer = False

#checks what the user inputs and proceeds to run the correct code
while correct_answer == False:
    answer = input("Please answer with 'preset' or 'random': ")
    if answer == 'random':
        correct_answer = True
        random_colors()
    if answer == 'preset':
        correct_answer = True
        preset_colors()
    else:
        print("That was not a valid answer. Please try again.")