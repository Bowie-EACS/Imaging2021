
#imports the function from two other scripts
#These functions run the original code
from Test_Run import functionTwo
from Image_Design_Challenge_october_fifth import functionOne

#Asks for user input on whether they was preset or random colors
print ("Would you like a preset of colors, or randomized colors?")
answer_valid = False


# If their answer is "Random", it will run the random color script
# If their answer is "Preset", it will run the preset color script 
# If their answer is not one of those, it will prompt them to re-enter an answer
while answer_valid == False:
    answer = input("Please answer with 'Preset', or 'Random':")
    if answer == 'Random':
        answer_valid = True
        functionTwo()  
    if answer == 'Preset':
        answer_valid = True
        functionOne()
    else:
        print ("Something was wrong with that answer. Please try again.")
        
