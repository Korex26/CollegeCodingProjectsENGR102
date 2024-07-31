# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Lilly Woodward
#               Kyle Rex
#               Jesse Garcia
#               Ethan Nguyen
# Section:      516
# Assignment:   Lab 9
# Date:         10 31 2022

def getpoints(string_input):  # turns input into a list of pairs
    pair_list = []
    pair_list0 = string_input.split()
    for i in pair_list0:
        newList = []
        i = i.split(',')
        for j in i:
          newList.append(int(j))
        pair_list.append(newList)
    return pair_list


def cross(first_point, second_point):  # cross product for each row
    crossp = float(first_point[0])*float(second_point[1]) - float(first_point[1])*float(second_point[0])
    return crossp


def shoelace(pair_list):  # adds all cross products and stops when it hits the last number
    sum_shoelace = 0
    pair_list.append(pair_list[0])  # adds starting point of polygon to complete calculation
    for j in range(len(pair_list)-1):
        sum_shoelace += cross(pair_list[j], pair_list[j+1])/2
    return sum_shoelace


def main():  # Takes the input then prints the answer.
    pair_string = input('Please enter the vertices: ')
    print(f'The area of the polygon is {shoelace(getpoints(pair_string))}')

if __name__ == '__main__':
    main()