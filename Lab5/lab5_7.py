sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_list = []

for t in sample_list:
    new_tuple = list(t)
    new_tuple[-1] = 100
    new_list.append(tuple(new_tuple))
print(new_list)
