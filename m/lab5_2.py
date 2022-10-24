string = input("Input string\n")
char_list = []
new_string = ""
for c in range(len(string)):
    if string[c] in char_list:
        new_string += "$"
    else:
        new_string += string[c]
        char_list.append(string[c])
print(new_string)
