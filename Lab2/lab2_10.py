# 10. Average of integers

n = int(input("Please input a integer:"))
i = 0
for x in range(n+1):
    i += x
print(f"Average for all integers I = 1, ... , N is : {i/n}")