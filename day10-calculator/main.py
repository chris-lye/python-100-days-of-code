import art
# Calculator

# Add
def add(n1,n2):
    return n1 + n2
    
# Subtract
def subtract(n1,n2):
    return n1 - n2

# Multiply
def multiply(n1,n2):
    return n1 * n2

# Divide
def divide(n1,n2):
    return n1 / n2

operations= {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    cont = True
    num1 = float(input("What's the first number?\n"))

    while cont:
        num2 = float(input("What's the second number?\n"))
        print("Choose an operation: \n+ - * /")
        op_sym = input("Pick a symbol above.\n")
        output = operations[op_sym](num1, num2)
        print(f"{num1} {op_sym} {num2} = {output}")
        cont = input(f"Type 'y' to continue with {output}. Type 'quit' to quit. Type anything else to do a new calculation.\n")
        if cont == "y":
            num1 = output
        elif cont == "quit":
            break
        else:
            calculator()

calculator()