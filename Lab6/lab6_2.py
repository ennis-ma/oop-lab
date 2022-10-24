for n in range(1, 51):
    if not n % 3 and not n % 5:
        print("Threevety")
    elif not n % 3:
        print("Threety")
    elif not n % 5:
        print("Fivety")
    else:
        print(n)
