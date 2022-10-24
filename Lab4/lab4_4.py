# print(len(input("Num: ")))

num = float(input("Num: "))
digit = 1
while num >= 10:
    num = num / 10
    digit += 1
print(digit)
