sample_list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
index_to_pop = [0, 4, 5]

index_to_pop.sort(reverse=True)
for i in index_to_pop:
    sample_list.pop(i)
print(sample_list)
