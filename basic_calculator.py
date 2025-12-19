def add(a, b):
    answer = a + b
    print(f"Answer result to: {answer}")

def multi(a, b):
    answer = a * b
    print(f"Answer result to: {answer}")

def div(a, b):
    answer = a / b
    print(f"Answer result to: {answer}")

def sub(a, b):
    answer = a - b
    print(f"Answer result to: {answer}")

print("A. ADDITION")
print("B. MULTIPLICATION")
print("C. DIVISION")
print("D. SUBTRACTION")

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
else:
    print("Invalid command")
    