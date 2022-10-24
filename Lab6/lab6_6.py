given_tuple = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
avg_list = []
for t in given_tuple:
    avg = 0
    for v in t:
        avg += v / len(t)
    avg_list.append(avg)
print(avg_list)
