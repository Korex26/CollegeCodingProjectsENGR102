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
# Date:         09/21/2022
paid_amount = float(input('How much did you pay?'))
cost_amount = float(input('How much did it cost?'))
change = paid_amount - cost_amount
change = 100 * round(change,2)
print(f'You received ${change/100:.2f} in change. That is...')

#quarters
if change >= 25:
    quarter = int(change//25)
    change -= quarter * 25
    if quarter == 0:
        pass
    elif quarter == 1:
        print(int(quarter), 'quarter')
    else:
        print(int(quarter), 'quarters')
#dimes
if change >= 10:
    dime = int(change//10)
    change -= dime * 10
    if dime == 0:
        pass
    elif dime == 1:
        print(int(dime), 'dime')
    else:
        print(int(dime), 'dimes')
#nickels
if change >= 5:
    nickel = int(change//5)
    change -= nickel * 5
    if nickel == 0:
        pass
    elif nickel == 1:
        print(int(nickel), 'nickel')
    else:
        print(int(nickel), 'nickels')
#pennies
if change >= 1:
    penny = int(change // 1)
    if penny == 0:
        pass
    elif penny ==1:
        print(int(penny), 'penny')
    else:
        print(int(penny), 'pennies')