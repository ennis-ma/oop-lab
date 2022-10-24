# 4. Simple calculator
import sys

# Looks way better
def ask_question(question: str):
    ans = input(question)
    if ans == "quit":
        print("Bye!")
        sys.exit()
    return ans

while True:
    num_1 = ask_question("Number 1: ")
    # if num_1 == "quit":
    #   break
    num_2 = ask_question("Number 2: ")
    # if num_2 == "quit":
    #   break
    op = ask_question("Operation (add, subtract, multiply, divide): ")
    # if ask_question == "quit":
    #   break

    
    # Solve by using if else.

    # if op == "add":
    #     ans = num_1 + num_2
    # elif op == "subtract":
    #     ans = num_1 - num_2
    # elif op == "multiply":
    #     ans = num_1 * num_2
    # elif op == "divide":
    #     ans = num_1 / num_2
    # else:
    #     print("Error, operation must be (add, subtract, multiply, divide)")

    # Solve by match case.
    match op:
        case "add":
            ans = num_1 + num_2
        case "subtract":
            ans = num_1 - num_2
        case "multiply":
            ans = num_1 * num_2
        case "divide":
            ans = num_1 / num_2
        case _:
            print("Error, operation must be (add, subtract, multiply, divide)")

    print(f"Ans: {ans}")
