def add(a, b):
    answer = a + b
    print(f"Answer result to: {answer}\n")

def multi(a, b):
    answer = a * b
    print(f"Answer result to: {answer}\n")

def div(a, b):
    answer = a / b
    print(f"Answer result to: {answer}\n")

def sub(a, b):
    answer = a - b
    print(f"Answer result to: {answer}\n")

while True:

    print("A. ADDITION")
    print("B. MULTIPLICATION")
    print("C. DIVISION")
    print("D. SUBTRACTION")
    print("E. Exit")

    choice = input("Choice: ")

    if choice == 'a' or choice == "A":
        a = int(input("Enter number: "))
        b = int(input("Enter number: "))
        add(a,b)
    elif choice == "b" or  choice =="A":
        a = int(input("Enter number: "))
        b = int(input("Enter number: "))
        multi(a,b)
    elif choice == "c" or choice == "C":
        a = int(input("Enter number: "))
        b = int(input("Enter number: "))
        div(a,b)
    elif choice == "d" or choice == "D":
        a = int(input("Enter number: "))
        b = int(input("Enter number: "))
        sub(a,b)
    elif choice == "e" or choice == "E":
        print("Thank you for using this program!\n")
        exit()
        
    else:
        print("Invalid command")