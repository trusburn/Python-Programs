
pin = 5050
balance = 50
def login(pin):
        for attempt in range(3):
            try:
                input_pin = int(input("Enter Pin: "))

                if input_pin == pin:
                    print("Login Successsful!\n")
                    return True
                else:
                    print("Incorrect Pin!")
            except ValueError:
                print("Numbers Only!")
        print("ATM Blocked")
        return False


login(pin)
exit()
while True:
    print("=== ATM MACHINE ===")
    try:
        intput_amount = int(input("Enter amount: "))
    except ValueError:
        print("Invalid character, Numbers only!")
        continue

    if intput_amount > balance:
        print("Fund balance")
        try:
            deposit = int(input("Deposit Amount: "))
        except ValueError:
            print("numbers only!")
            continue
        balance += deposit
        print(f"Deposit successful! balance is {balance}")
        continue
        

    balance -= intput_amount
    print(f"transaction of {intput_amount}succesful")
    print(f"Your new balance is now {balance}")
    break