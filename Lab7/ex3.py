user_input = int(input("N: "))


def average(n: int):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total / n


print(f"For N={user_input}, the average is {average(user_input)}")
