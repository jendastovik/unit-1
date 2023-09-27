# Crypto Wallet

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

An example of the data stored is 

| Date | Description | Category | Amount  |
|------|-------------|----------|---------|
| Sep 23 2022 | bought a house | Expenses | 10 BTC |
| Sep 24 2022 | food for house celebration | Food | 0.000001 BTC |


## Proposed Solution

Design statement:
I will to design and make an electronic ladger for a client who is Mr. Sato. The ladger will about Tether and is constructed using the software Python. It will take  a week to make and will be evaluated according to the criteria below

## About Tether

Launched in 2014, Tether is a blockchain-enabled platform designed to facilitate the use of fiat currencies in a digital manner. Tether works to disrupt the conventional financial system via a more modern approach to money. Tether has made headway by giving customers the ability to transact with traditional currencies across the blockchain, without the inherent volatility and complexity typically associated with a digital currency. As the first blockchain-enabled platform to facilitate the digital use of traditional currencies (a familiar, stable accounting unit), Tether has democratised cross-border transactions across the blockchain.


## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the cyrptocurrency selected.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The electronic ledger allows to display the current balance.
5. The electronic ledger allows to display the transaction history, which can be filtred by date, category or amount in certain range.
6. You can switch between different users with different transactions, every user has it's own password and username.

# Criteria B: Design

## System Diagram
![](/Project/diagram2.png)


## Flow Diagrams
flow diagram for the try_login function

![](/flowCharts/try_login.png)

flow diagram for the do_login function

![](/flowCharts/do_login.png)

flow diagram for find_bydate function (works the same for find_bydescription and find_byamount)

![](/flowCharts/Find_ByDate.png)

## Record of Tasks
| Task No | Planned Action           | Planned Outcome                                                                          | Time estimate | Target completion date | Criterion |
|---------|--------------------------|------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram    | To have a clear idea of the hardware and software requirements for the proposed solution | 10min         | Sep 8                  | B         |
| 2       | Create login system      | To have a flow diagram and the code for login                                            | 30min         | Sep 14                 | B, C      |
| 3       | Create filtration system | To have a functional system and flowchart for saving and filtering transactions          | 30min         | Sep 17                 | B, C      |
| 4       | Add and del tran.        | To have system to delete and add transactions for different users                        | 15min         | Sep 18                 | C         |
| 5       | Create colours           | To have different colour coding in terminal and make visualisation clearer               | 10min         | Sep 19                 | C         |
| 6       | Edit text visualisation  | To save all most of the texts into txt. files                                            | 15min         | Sep 20                 | C         |

# Criteria C: Development
All the functions are commented in the code in files operations.py and project.py

## Login System
My client requires a system to protect the private data. I thought about using a login system to accomplish this requirement using a if condition and the open command to work with a csv file. The csv file contains the username and password of the user. The code is the following:
```python
def try_login(username:str, password:str) -> bool:
    with open ("/Project/users.csv", "r") as f:
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
        print("You have {attempts} attempts left")
        input_username = input("Username: ")
        input_password = input("Password: ")
        result = try_login(input_username, input_password)
```
## Saving transactions
My client requires a system to save the transactions. I thought about using a json file to accomplish this requirement. Json is more practical than csv because it allows to save the data in a dictionary format and allows to create different transaction lists for different users. The json file of every single user contains list of transactions with the date, description, category and amount of the transaction. The code is the following:
```python
def load_transactions(user:str):
    with open("Project/transactions.json", "r") as f:
        data = json.load(f)
    dates = []
    amounts = []
    descriptions = []
    for tran in data[user]:
        dates.append(tran["date"])
        amounts.append(tran["amount"])
        descriptions.append(tran["description"])
        #print(f"{tran['date']}: {tran['amount']}, {tran['description']}")
    return dates, amounts, descriptions

def add_transaction(date, amount, description, user):
    with open("Project/transactions.json", "r") as f:
        data = json.load(f)
    data[user].append({"date": date, "amount": amount, "description": description})
    with open("Project/transactions.json", "w") as f:
        json.dump(data, f, indent=4)

def Delete_Transaction(date, amount, description, user):
    with open("Project/transactions.json", "r") as f:
        data = json.load(f)
    deleted = False
    for tran in data[user]:
        if tran["date"] == date and tran["amount"] == amount and tran["description"] == description:
            data[user].remove(tran)
            deleted = True
            colours.pGreen("Transaction deleted")
    if not deleted:
        colours.pRed("Transaction not found")
    with open("Project/transactions.json", "w") as f:
        json.dump(data, f, indent=4)
```
## Filtering transactions
My client requires a system to filter the transactions. I thought about using a function to filter the transactions by date, category or amount in certain range. The code is the following:
```python
def Find_ByDate(dates, amounts, descriptions, date):
    ret_amounts = []
    ret_descriptions = []
    for i in range(len(dates)):
        if dates[i] == date:
            ret_amounts.append(amounts[i])
            ret_descriptions.append(descriptions[i])
    return ret_amounts, ret_descriptions

def Find_ByDescription(dates, amounts, descriptions, description):
    ret_dates = []
    ret_amounts = []
    for i in range(len(descriptions)):
        if descriptions[i] == description:
            ret_dates.append(dates[i])
            ret_amounts.append(amounts[i])
    return ret_dates, ret_amounts

def Find_ByAmount(dates, amounts, descriptions, minamount, maxamont):
    ret_dates = []
    ret_descriptions = []
    ret_amounts = []
    for i in range(len(amounts)):
        if int(amounts[i]) >= minamount and int(amounts[i]) <= maxamont:
            ret_dates.append(dates[i])
            ret_descriptions.append(descriptions[i])
            ret_amounts.append(amounts[i])
    return ret_dates, ret_descriptions, ret_amounts
```

## viewing txt. files
My client requires a system with which he/she can interact and that requires some text visualisation. I thought about using a txt. file to accomplish this requirement, which would eventualy allow also translation into different languages. The txt. file contains the basic description of the cryptocurrency selected or from which client can choose. The code is the following:
```python
def print_text_file(filename:str):
    with open(filename, "r") as f:
        data = f.readlines()
    for line in data:
        print(line.strip())
```
## Running program
All the functions are called in the main function, which also takes care of most of the communication with the user. The code is the following:
```python
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
```

