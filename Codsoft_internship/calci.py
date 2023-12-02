import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
opn_dict={
    "+":add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    n1=float(input("Enter the first number: "))
    for symbol in opn_dict:
        print(symbol)
    
    continue_flag= True
    while continue_flag:
        op_symb = input("Choose any operation: ")
        n2=float(input("Enter next number: "))
        calc_function=opn_dict[op_symb]
        output=calc_function(n1,n2)
        print(f"{n1} {op_symb} {n2} = {output} ")
        should_continue=input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit ").lower()
        if should_continue=='y':
            n1=output
        elif should_continue=='n':
            continue_flag=False
            os.system('cls')
            calculator()
        else:
            continue_flag=False
            print("Exit :)")
calculator()
        