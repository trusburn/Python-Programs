#collect inputs

def main():
    print("=== This is a monthly payment loan calculator")
    print("")

    principal = float(input("Enter loan amount: "))
    apr = float(input("Enter the annual interest rate: "))
    year = int(input("Enter amount of Years: "))


    monthly_interest_rate = apr / 1200
    month = years * 12