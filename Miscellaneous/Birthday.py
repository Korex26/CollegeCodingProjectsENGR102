#Write a program that lets a user enter a date, in a string of the form: month/day/year. 
#The program then converts the entered date to the format mmm dd, yyyy, and displays it.
a = input("Enter the date of your birthday(month/day/year): ")
#input 11 06 2003
a = a.split()
Dictionary = {"1":"Jan", "2": "Feb", "3": "Mar", "4": "Apr", "5": "May", "6": "Jun", "7": "Jul", "8": "Aug", "9": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}
if a[0] not in Dictionary:
    print("You typed in your birthday incorrectly")
if a[0] in Dictionary: #these all add onto the original print statement to give the correctly formated answer
    a[0] = Dictionary[a[0]]
    print(f"{a[0]} {a[1]}, {a[2]}" )
print(" ", end="") 
    

