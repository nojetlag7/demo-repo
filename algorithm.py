#reverse number
""" 
rev_num = 0
 number = int(input("Please input number: "))

 while number != 0:
     last_digit = number % 10
     rev_num = (rev_num * 10) + last_digit
     number = number // 10

 print(rev_num)
"""

# DISTANCE Question
'''
distance = int(input("Enter distance travelled: "))
miles = int(distance / 5280)
milesrem = distance % 5280
yards = int(distance / 3)
yardrem = distance % 3
feet = yardrem
if miles > 0:
    if miles == 1:
        print(f'{miles} mile', end=" ")
    else:
        print(f'{miles} miles', end=" ")
if yards > 0:
    if yards == 1:
        print(f'{yards} yard', end=" ")
    else:
        print(f'{yards} yards', end=" ")
if feet > 0:
    if feet == 1:
        print(f'{feet} foot',)
    else:
        print(f'{feet} feet')
'''

# program for formatting currency
"""
amount = float(input("Input amount: "))
whole_p = int(amount)
deci_p = int(round((amount - whole_p) * 100, 2))
i = 0
stramount = "."
while whole_p > 0:
    lastdigit = whole_p % 10
    stramount = str(lastdigit) + stramount
    whole_p = int(whole_p / 10)
    i += 1
    if deci_p > 0:
        if i % 3 == 0:
            stramount = ',' + stramount
if deci_p > 9:
    print(stramount + str(deci_p))
else:
    print(stramount + '0' + str(deci_p))
"""

#Square root aproxx.
'''
Num = float(input("Please input number: "))
lg = float(input("Guess the sqrt of the number given: "))
ng = lg
while True:
    lg = ng
    ng = 0.5 * (lg + Num / lg)
    if abs(lg - ng) < pow(10, -7):
        break
print(f'The approximate square root of the number is {lg}')
'''

#Bubble sort
'''n = int(input("Enter size of array: "))
array = [8,6,5,4,9,2,1,12,36,29,4,6]

for i in range(0, n):
    for j in range(0, n-i-1):
        if array[j] > array[j+1]:
            c = array[j]
            array[j] = array[j+1]
            array[j+1] = c
print(array)
'''

while True:
    try:
        number = int(input("Enter a number to be used for the program: "))
    except ValueError:
        print("Invalid input. Enter a number.")
    else:
        break
if number % 3 ==0  and number % 5== 0:
    print("FizzBuzz")
elif number % 5 == 0:
    print("Buzz")
elif  number % 3 == 0:
    print("Fizz")
else:
    print("done") 