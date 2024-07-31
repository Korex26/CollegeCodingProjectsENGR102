# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 10
# Date:         11/10/2022
#
def high():
        print('Too high!')
def low():
        print('Too low!')
print("Guess the secret number! Hint: it's an integer between 1 and 100...")
correct_num = 26
input_num = 1
num_guesses = 0  
i = 0
while input_num != correct_num:  
    try: #use try to look for errors
        if i == 0:
            input_num = int(input('What is your guess? '))
            num_guesses += 1
        if i == 1:
            input_num = int(input('Bad input! Try again: '))
            num_guesses += 1
            i = 0
    except ValueError:   #if errors found, run this code
        try:
            input_num = int(input('Bad input! Try again: '))
            num_guesses += 1
            i = 0
        except ValueError:
            i += 1
            continue
    if input_num > correct_num:
        high()
    elif input_num < correct_num:
        low()
    elif input_num == correct_num:
        i += 1
        print('You guessed it! It took you', num_guesses, 'guesses.')