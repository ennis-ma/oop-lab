import math


line = int(input("Num: "))
for i in range(1, line+1):
    if i <= math.ceil(line/2):
        print("*"*i)
    else:
        print("*"*(line-i+1))
