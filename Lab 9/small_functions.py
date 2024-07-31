# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 9a
# Date:         10/14/2022
#

############# PART A #############
import math
#r_sphere = float(input("What is the radius of the sphere:" ))
# input 3
#r_hole = float(input("What is the radius of the hole:"))
# input 2
def parta(r_sphere,r_hole):
    
    a = r_hole
    r = r_sphere
    h = r - (r**2 - a**2)**(1/2)
    Volume_spherical_cap = (((math.pi)*(h**2))/3)*(3*r - h)
    Volume_of_cylinder = (math.pi)*(a**2)*(((r**2 - a**2)**(1/2))*2)
    Volume_of_sphere = ((4/3)*(math.pi)*((r)**3))
    Volume_of_bead = Volume_of_sphere - Volume_of_cylinder - (Volume_spherical_cap *2)
    #equation for volume of sphere with hole down middle
    
    
    return Volume_of_bead
    #print("The volume of the bead is:", parta(r_sphere,r_hole))



############# PART B #############
#n = float(input("Type a positive integer:" ))
#input 675
def partb(n):
    a = 1
    list=[]
    while(a<n):
        if(n - (a + (a +2))) == 0:
            list.append(a)
            list.append(a + 2)
            a+=2
        if(n - (a + ((a +2)+(a+4)))) == 0:
            list.append(a)
            list.append(a + 2)
            list.append(a + 4)
            a+=2
        else:
            a += 2
    if (list == []):
        return(bool(False))
    else:
        return(list)
    #print("The list of consecutive numbers that can be multiplied to get your number are:", partb(n))



############# PART C #############
#character = input("Please input a single character:")
# input *
#name = input("Please input a person’s name:")
# input Dr. Ritchey
#company = input("Please input a company:")
# input Texas A&M University
#email = input("Please input a email:")
# input snrichey@tamu.edu

def partc(character, name, company, email):
    list = [character, name, company, email]
    space = " " 
    if (len(list[0]) > len(list[1]) and len(list[0]) > len(list[2]) and len(list[0]) > len(list[3])):
        card_length = len(list[0])
    elif (len(list[1]) > len(list[0]) and len(list[1]) > len(list[2]) and len(list[1]) > len(list[3])):
        card_length = len(list[1])
    elif (len(list[2]) > len(list[0]) and len(list[2]) > len(list[1]) and len(list[2]) > len(list[3])):
        card_length = len(list[2])
    elif (len(list[3]) > len(list[1]) and len(list[3]) > len(list[2]) and len(list[3]) > len(list[0])):
        card_length = len(list[3])
    card_length = int(card_length)
    
    if ((len(list[1]) % 2) != 0):
        a = 2
    else:
        a = 1
    biz_card_top = character*(card_length + (4+a))
    biz_card_bottom = character*(card_length + (4+a))
    
    
    b = (biz_card_top)
    
    
    if ((len(list[1]) % 2) != 0):
        a = (space + character)
    else:
        a = (character)
    c = ((character + space*(((card_length +4) - len(list[1]))//2)) + name + (space*(((card_length + 4) - len(list[1]))//2)) + a)
    if ((len(list[2]) % 2) != 0):
        a = (space + character)
    else:
        a = (character)
    d = ((character + space*(((card_length +4) - len(list[2]))//2)) + company + (space*(((card_length +4) - len(list[2]))//2)) + a)   
    if ((len(list[3]) % 2) != 0):
        a = (space + character)
    else:
        a = (character)
    e = ((character + space*(((card_length +4) - len(list[3]))//2)) + email + (space*(((card_length +4) - len(list[3]))//2)) + a)
    
    if ((len(list[1]) % 2) != 0):
        a = (character + character)
    else:
        a = (character)
    
    f = (biz_card_bottom)
    my_tuple = (b,c,d,e,f).split(",")
    return("\n".join(my_tuple))
    
#b1,c2,d3,e4,f5 = partc(character, name, company, email)


    #partc(character, name, company, email)



############# PART D #############
#List_of_numbers = input("Please type a list of numbers separated by spaces:")
#input 25 89 56 78 98 100 for first iteration
#input 25 89 56 78 98 for second iteration
def partd(List_of_numbers):
    #List_of_numbers = List_of_numbers.split()
    #List_of_numbers = [int(i) for i in List_of_numbers]
    List_of_numbers.sort()
    
    if(len(List_of_numbers) % 2 == 0):
        a = ((((int(List_of_numbers[(len(List_of_numbers)//2)]) - int(List_of_numbers[(len(List_of_numbers)//2) - 1]))/2) + int(List_of_numbers[(len(List_of_numbers)//2) - 1])))
    else:
        a = (List_of_numbers[(len(List_of_numbers)//2)])
    return(List_of_numbers[0],a,List_of_numbers[(len(List_of_numbers) - 1)])
    #return(List_of_numbers[(len(List_of_numbers) - 1)])
    
#partd(List_of_numbers)



############# PART E #############
#List_of_times = input("Please enter a list of times in increasing order:")
# input 10 20 30 40 50
#List_of_distances = input("Please enter the distance traveled which coresponds with each time:")
# input 25 50 75 100 125
def parte(List_of_times,List_of_distances):
    #List_of_times = List_of_times.split()
    #List_of_times = [float(i) for i in List_of_times]
    #List_of_distances = List_of_distances.split()
    #List_of_distances = [float(i) for i in List_of_distances]
    List_of_velocities = []
    for i in range(len(List_of_times)-1):
        velocity = ((List_of_distances[i+1]) - (List_of_distances[i]))/((List_of_times[i+1]) - (List_of_times[i]))
        List_of_velocities.append(velocity)
    return List_of_velocities
#print(parte(List_of_times,List_of_distances))



############# PART F #############
#List_of_numbers = input("Please type a list of numbers separated by spaces:")
# input 2000 26
# input 6 7
def partf(List_of_numbers):
    #List_of_numbers = List_of_numbers.split()
    List_of_numbers = [int(i) for i in List_of_numbers]
    List_of_numbers.sort()
    a = 0
    b = 0
    List = []
    while(a<len(List_of_numbers)):
        while(b<len(List_of_numbers)):
            if((List_of_numbers[a] + List_of_numbers[b]) == 2026):
                List.append(List_of_numbers[a] * List_of_numbers[b])
                break
            else:
                b+=1
        a += 1
    if (List == []):
        return(bool(False))
    else:
        return(List[0])

#print(partf(List_of_numbers))






