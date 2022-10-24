# 5. Multiples

from math import remainder


num_1 = int(input("First number: "))
num_2 = int(input("Second number: "))
remainder = num_2%num_1
if remainder == 0:
    print("First number is the multiple of the second number")
    print(num_2/num_1)
else:
    print("First number is NOT the multiple of the second number")
    print(f"Remainder is {remainder}")