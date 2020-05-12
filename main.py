import json


def main():
    fd_list = []
    rd_list = []
    main_menu_choice = 0
    while main_menu_choice != 3:
        main_menu_choice = main_menu()
        if main_menu_choice == 1:
            fd_menu(fd_list)
        elif main_menu_choice == 2:
            rd_menu(rd_list)
    else:
        SystemExit()


def main_menu():
    choice = 0
    while choice not in range(1, 4):
        print("******************************")
        print("  Bank Account Demonstration  ")
        print("******************************")
        print("1. Fixed Deposit")
        print("2. Recurring Deposit")
        print("3. Exit")
        choice = int(input("Enter you choice in number: "))
        if choice not in range(1, 4):
            print("Wrong option, please try again.")
    print("\n")
    return choice


def fd_menu(fd_list):
    print("~~~ FIXED DEPOSIT MENU ~~~")
    account_number = int(input("Enter the account number: "))
    check = next(
        (item for item in fd_list if item["account_number"] == account_number), None
    )
    if not check == None:
        print("Entry already exists. Here are the details:\n")
        print(json.dumps(check, indent=4))
    else:
        name = str(input("Enter the account holder's name: "))
        principal_amount = int(input("Enter the principal amount: "))
        interest_rate = int(input("Enter the interest rate: "))
        term = int(input("Enter the term period: "))
        amount = principal_amount + (principal_amount * term * interest_rate / 100)
        print("The maturity amount after", term, "years will be Rs.", amount)
        fd = {
            "account_number": account_number,
            "name": name,
            "principal_amount": principal_amount,
            "interest_rate": interest_rate,
            "term": term,
            "amount": amount,
        }
        fd_list.append(fd)
    print("\n")


def rd_menu(rd_list):
    print("~~~ RECURRING DEPOSIT MENU ~~~")
    account_number = int(input("Enter the account number: "))
    check = next(
        (item for item in rd_list if item["account_number"] == account_number), None
    )
    if not check == None:
        print("Entry already exists. Here are the details:\n")
        print(json.dumps(check, indent=4))
    else:
        name = str(input("Enter the account holder's name: "))
        monthly_amount = int(input("Enter the monthly amount: "))
        interest_rate = int(input("Enter the interest rate: "))
        term = int(input("Enter the term period: "))
        amount = monthly_amount * ((1 + interest_rate) * term - 1) / 1 - (
            1 + interest_rate
        )
        print("The maturity amount after", term, "years will be Rs.", amount)
        rd = {
            "account_number": account_number,
            "name": name,
            "monthly_amount": monthly_amount,
            "interest_rate": interest_rate,
            "term": term,
            "amount": amount,
        }
        rd_list.append(rd)
    print("\n")


main()
