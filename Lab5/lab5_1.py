string = input("Input string\n")
if len(string) < 2:
    print("Empty String")
else:
    result = f"{string[:2]}{string[-2:]}"
    print(result)
