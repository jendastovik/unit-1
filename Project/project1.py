import operations
from colours import *

def try_login(username:str, password:str) -> bool:
    """
    checks if the username and password are in the users.csv file
    """
    with open ("Project/users.csv", "r") as f:
        data = f.readlines()
    for line in data:
        line = line.strip().split(",")
        if username == line[0] and password == line[1]:
            pGreen("Login successful")
            return True
    pRed("Login failed")
    return False

def do_login():
    """
    gives the user 3 attempts to login and returns username and result
    """
    attempts = 3
    input_username = input("Username: ")
    input_password = input("Password: ")
    result = try_login(input_username, input_password)
    while not result and attempts > 1:
        attempts -= 1
        pRed(f"You have {attempts} attempts left")
        input_username = input("Username: ")
        input_password = input("Password: ")
        result = try_login(input_username, input_password)
    return result, input_username

def print_text_file(filename:str):
    """
    prints selected text file
    """
    with open(filename, "r") as f:
        data = f.readlines()
    for line in data:
        print(line.strip())

def view_transactions(username:str):
    """
    prints the transactions of a user and gives the user the option to filter the transactions
    """
    print_text_file("Project/texts/op2.txt")
    dates, amounts, descriptions = operations.load_transactions(username)
    choice = input("Enter your choice: ")
    if choice == "1":
        date = input("Enter date: ")
        amounts, descriptions = operations.Find_ByDate(dates, amounts, descriptions, date)
        pGreen(f"transactions for the date {date} are the following:")
        for i in range(len(amounts)):
            print(f"{amounts[i]}, {descriptions[i]}")
    elif choice == "2":
        description = input("Enter description: ")
        dates, amounts = operations.Find_ByDescription(dates, amounts, descriptions, description)
        pGreen(f"transactions for the description '{description}' are the following:")
        for i in range(len(dates)):
            print(f"{dates[i]}, {amounts[i]}")
    elif choice == "3":
        minamount = int(input("Enter min amount: "))
        maxamount = int(input("Enter max amount: "))
        dates, descriptions, amounts = operations.Find_ByAmount(dates, amounts, descriptions, minamount, maxamount)
        pGreen(f"transactions for the amount between {minamount} and {maxamount} are the following:")
        for i in range(len(dates)):
            print(f"{dates[i]}, {amounts[i]}, {descriptions[i]}")
    elif choice == "4":
        pGreen(f"All {len(dates)} transactions are the following:")
        for i in range(len(dates)):
            print(f"{dates[i]}, {amounts[i]}, {descriptions[i]}")


def main():
    """
    main function, goes through the program, 
    gives the user the option to login
    then view transactions, add transactions, delete transactions, view balance and exit
    """
    result, username = do_login()
    if not result:
        pRed("You have exceeded the number of attempts")
        return
    print(f"Welcome to the virtual lager, {username}\n")
    print_text_file("Project/texts/teather.txt")
    continue_program = True
    while continue_program:
        print()
        print_text_file("Project/texts/op1.txt")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_transactions(username)
        elif choice == "2":
            date = input("Enter date: ")
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            operations.add_transaction(date, amount, description, username)
        elif choice == "3":
            date = input("Enter date: ")
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            try:
                operations.Delete_Transaction(date, amount, description, username)
            except:
                pRed("Transaction not found")
        elif choice == "4":
            dates, amounts, descriptions = operations.load_transactions(username)
            pGreen(f"Total balance is: {operations.Balance(amounts)}")
        elif choice == "5":
            continue_program = False
        
            
                
main()
            
        
    