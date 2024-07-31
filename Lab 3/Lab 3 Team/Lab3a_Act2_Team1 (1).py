# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kyle Rex
#               Ethan Nguyen
#               Jesse Garcia
#               Lilly Woodward
# Section:      516
# Assignment:   Lab 2a - team
# Date:         09/14/2022
w = input('Enter name of group member 1: ') #enter 'Jesse Garcia' for  name, enter 'California' for fav place, enter '7' for fav number
x = input('Enter name of group member 2: ') #enter 'Ethan Nguyen' for  name, enter 'Home' for fav place, enter '404' for fav number
y = input('Enter name of group member 3: ') #enter 'Lilly Woodward' for  name, enter 'PK Lake' for fav place, enter '3' for fav number
z = input('Enter name of group member 4: ') #enter 'Kyle Rex' for  name, enter 'Tee Lake Michigan' for fav place, enter '55' for fav number

names = [w, x, y, z]
fav_place = [input(f'What is {w}\'s favorite place?: '), input(f'What is {x}\'s favorite place?: '), input(f'What is {y}\'s favorite place?: '), input(f'What is {z}\'s favorite place?: ')]
fav_num = [input(f'What is {w}\'s favorite number?: '), input(f'What is {x}\'s favorite number?: '), input(f'What is {y}\'s favorite number?: '), input(f'What is {z}\'s favorite number?: ')]

print(names[0], 10*" ", names[1], 12*" ", names[2], 12*" ", names[3])
print(fav_place[0], (10-(len(fav_place[0]) - len(names[0])))*" ", fav_place[1], (12-(len(fav_place[1]) - len(names[1])))*" ", fav_place[2], (12-(len(fav_place[2]) - len(names[2])))*" ", fav_place[3])
print(fav_num[0], (10+(len(names[0]) - len(fav_num[0])))*" ", fav_num[1], (12+(len(names[1]) - len(fav_num[1])))*" ", fav_num[2], (12+(len(names[2]) - len(fav_num[2])))*" ", fav_num[3])