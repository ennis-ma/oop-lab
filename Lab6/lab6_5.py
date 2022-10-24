og_dict = {1: "red", 2: "green", 3: "black", 4: "white", 5: "black"}
new_dict = {v: len(v) for v in og_dict.values()}
print(new_dict)
