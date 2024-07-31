# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 7b
# Date:         10/14/2022
#
initial_num = input("Enter a four-digit integer: ")
kaprekar = initial_num
t = 0  #number of iterations

#converting to int
list_hl = [int(i) for i in initial_num]
list_lh = [int(i) for i in initial_num]

while len(list_hl) != 4:
    list_hl.append(int(0))
    

list_hl.sort(reverse = True) #sorts reverse
list_lh.sort() #sorts regular from lowest to highest

if list_hl[0] == list_hl[1] and list_hl[0] == list_hl[2] and list_hl[0] == list_hl[3]: 
    print(f'{initial_num} > 0')
    print(f'{initial_num} reaches 0 via Kaprekar\'s routine in 1 iterations')
else:
    for x in list_hl:
        list_hl_str = [str(x) for x in list_hl]
        list_hl_int = int("".join(list_hl_str)) # coverting the lists back to integers
    for x in list_lh:
        list_lh_str = [str(x) for x in list_lh]
        list_lh_int = int("".join(list_lh_str))
        
    
    while kaprekar != 6174:
        print(kaprekar, end=" > ")
        kaprekar = list_hl_int - list_lh_int #subtracting smaller number from bigger number
        t += 1 #adds 1 to iterations each time
         
        hl = str(kaprekar) #converts to string
        lh = str(kaprekar)
        
        list_hl = [int(i) for i in hl] # converts to int
        list_lh = [int(i) for i in lh]
        
        while len(list_hl) != 4:
            list_hl.append(int(0))
            
        list_hl.sort(reverse = True) # resorts them
        list_lh.sort()
        
        for x in list_hl:
            list_hl_str = [str(x) for x in list_hl] 
            list_hl_int = int("".join(list_hl_str)) #converts to int again
        for x in list_lh:
            list_lh_str = [str(x) for x in list_lh]
            list_lh_int = int("".join(list_lh_str))
    print(kaprekar)
    
    print(f'{initial_num} reaches 6174 via Kaprekar\'s routine in {t} iterations')# prints out the values with the correct formating
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    