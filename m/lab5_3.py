START_WORD = "not"
END_WORD = "poor"

string = input("Input string\n")
start = string.find(START_WORD)
end = string.find(END_WORD) + len(END_WORD)
if start != -1 and end != -1:
    print(f"{string[:start]}good{string[end:]}")
else:
    print(string)
