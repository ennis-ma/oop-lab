word_list = ["Red", "Green", "Blue", "White", "Black"]
rev_word_list = []
for word in word_list:
    rev_word = ""
    for i in range(len(word) - 1, -1, -1):
        rev_word += word[i]
    rev_word_list.append(rev_word)
print(rev_word_list)
