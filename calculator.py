def calc():
    num_1 = int(input("Please input your first number: "))
    num_2 = int(input("Please input your second number: "))
    oper = input("Finally, name the operation that you would like to perform (add, subtract, multiply, divide): ")
    # +
    if (oper == "add"):
        result = num_1 + num_2
        print(f"The sum of {num_1} and {num_2} is {result}.")

    # -
    elif oper == "subtract":
        result = num_1 - num_2
        print(f"{num_1} minus {num_2} is {result}.")

    # *
    elif oper == "multiply":
        result = num_1 * num_2
        print(f"{num_1} times {num_2} is {result}.")

    # /
    elif oper == "divide":
        result = num_1 / num_2
        print(f"{num_1} divided by {num_2} is {result}.")
