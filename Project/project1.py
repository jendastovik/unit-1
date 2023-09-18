import operations

def try_login(username:str, password:str) -> bool:
    with open ("Project/users.csv", "r") as f:
        data = f.readlines()
    for line in data:
        line = line.strip().split(",")
        if username == line[0] and password == line[1]:
            print("Login successful")
            return True
    print("Login failed")
    return False

def do_login():
    attempts = 3
    input_username = input("Username: ")
    input_password = input("Password: ")
    result = try_login(input_username, input_password)
    while not result and attempts > 0:
        attempts -= 1
        print(f"You have {attempts} attempts left")
        input_username = input("Username: ")
        input_password = input("Password: ")
        result = try_login(input_username, input_password)
    return result, input_username

def main():
    result, username = do_login()
    if not result:
        print("You have exceeded the number of attempts")
        return
    print(f"Welcome to the virtual lager, {username}")
    continue_program = True
    while continue_program:
        print("1. View transactions (by date, description, amount)")
        print("2. Add transaction")
        print("3. Delete transaction")
        print("4. View balance")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("1. View transactions by date")
            print("2. View transactions by description")
            print("3. View transactions by amount")
            print("4. View all transactions")
            dates, amounts, descriptions = operations.load_transactions(username)
            choice = input("Enter your choice: ")
            if choice == "1":
                date = input("Enter date: ")
                amounts, descriptions = operations.Find_ByDate(dates, amounts, descriptions, date)
                for i in range(len(amounts)):
                    print(f"{amounts[i]}, {descriptions[i]}")
            elif choice == "2":
                description = input("Enter description: ")
                dates, amounts = operations.Find_ByDescription(dates, amounts, descriptions, description)
                for i in range(len(dates)):
                    print(f"{dates[i]}, {amounts[i]}")
            elif choice == "3":
                minamount = int(input("Enter min amount: "))
                maxamount = int(input("Enter max amount: "))
                dates, descriptions = operations.Find_ByAmount(dates, amounts, descriptions, minamount, maxamount)
                for i in range(len(dates)):
                    print(f"{dates[i]}, {descriptions[i]}")
            elif choice == "4":
                for i in range(len(dates)):
                    print(f"{dates[i]}, {amounts[i]}, {descriptions[i]}")

main()
            
        
    