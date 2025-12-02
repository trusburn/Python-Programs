pin = 5050
balance = 5000

print("===== ATM MACHINE =====")
input_pin = int(input("Enter pin: "))

if input_pin != pin:
    print("incorrect pin")
    exit()

amount = int(input("Enter amount: "))

if amount > balance or amount <= 0:
    print("You need to top up")
    deposit = int(input("How much would you like to depsoit: "))
    balance += deposit
    print(f"Deposit complete! Your balance is now: {balance}")
    amount = int(input("How much would you like to withdraw now: "))
    balance -= amount
    print("Withdrawal Succesfull✅")
    print(f"Withdrawn amount: {amount}")
    print(f"Balance is now:  {balance}")
    exit()
else:
    balance -= amount
    print("Withdrawal Succesfull✅")
    print(f"Withdrawn amount: {amount}")
    print(f"Balance is now:  {balance}")