one = float(input("Number 1: "))
two = float(input("Number 2: "))
op = input("Op: ")
ans = 0


def add(num1: float, num2: float):
    return num1 + num2


def subtract(num1: float, num2: float):
    return num1 - num2


def multiply(num1: float, num2: float):
    return num1 * num2


def divide(num1: float, num2: float):
    return num1 / num2


match op.lower():
    case "add":
        ans = add(one, two)
    case "subtract":
        ans = subtract(one, two)
    case "multiply":
        ans = multiply(one, two)
    case "divide":
        ans = divide(one, two)
    case _:
        print("Wrong op")

print(ans)
