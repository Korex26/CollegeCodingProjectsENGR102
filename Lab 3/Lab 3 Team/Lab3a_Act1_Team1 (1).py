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
conv = float(input("Please enter the quantity to be converted:"))
newt = conv*4.44822
miles = conv*0.62137
kP = conv* 760
BTU = conv*3.41214
gal = conv* 0.2641721 * 60
print(f"{conv:.2f} pounds force is equivalent to {newt:.2f} Newtons")
print(f"{conv:.2f} kilometers is equivalent to {miles:.2f} miles")
print(f"{conv:.2f} atmospheres is equivalent to {kP:.2f} millimeters of mercury")
print(f"{conv:.2f} watts is equivalent to {BTU:.2f} BTU per hour")
print(f"{conv:.2f} liters per second is equivalent to {gal:.2f} US gallons per minute")

