import math


start = int(input("start:"))
end = int(input("end:"))
print(f"Prime numbers between {start} and {end} are: ")

for i in range(start,end):
    prime = True
    if i <= 1:
        prime = False
    for j in range(2, math.floor((i+1)/2)):
        if i % j == 0:
            prime = False
    if prime:
        print(i)