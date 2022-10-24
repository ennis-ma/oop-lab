given_tuple = ((1, 2, 3), (4, 5, 6), (7, 8))
for t in given_tuple:
    avg = 0
    for v in t:
        avg += v / len(t)
    print(avg)
