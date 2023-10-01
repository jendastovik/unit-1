# Crypto Wallet
![](/Project/tether_cover.png)
<sub> image source: https://blocktrade.com/learn/the-best-tether-wallet-a-2023-review/ </sub>

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
4. The electronic ledger allows to display the transaction history, which can be filtred by date, category or amount in certain range and display current balance.
5. You can switch between different users with different transactions, every user has it's own password and username.
6. Password protected by hashing and salt.

## Justification of the solution
### Programming language - Python
Python is a programming language that lets you work quickly and integrate systems more effectively. It is a high-level programming language, with simple syntax and dynamic typing, making it an ideal language for scripting and rapid application development. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available.

### Text-based software
Text-based software is a software that runs in the terminal. It is a software that is easy to use and does not require any graphical user interface. It is also easy to use for the developer, because it does not require any additional libraries. It is also easy to use for the client, because it does not require any additional installations and can be run on any computer.

### Json file
It allows to save the data in a dictionary format and allows to create different transaction lists for different users. It is also easy to use for the developer, because it does not require any additional libraries. It is also easy to use for the client, because it does not require any additional installations and can be run on any computer.

### Hash encoding
Hash encoding is a method of protecting passwords. It is a one-way function, which means that it is impossible to decode the password. It is also easy to use for the developer, because it does not require any additional libraries. It is also easy to use for the client, because it does not require any additional installations and can be run on any computer.

## Citations
https://tether.to/about-us/
https://www.python.org/doc/essays/blurb/
https://www.techopedia.com/definition/28178/text-based
https://www.w3schools.com/python/python_json.asp
https://www.geeksforgeeks.org/hashing-passwords-python/

# Criteria B: Design

## System Diagram
![](/Project/diagram2.png)


## Flow Diagrams
### Flow diagram for the try_login function

![](/flowCharts/try_login.png)

### Flow diagram for the do_login function

![](/flowCharts/do_login.png)

### Flow diagram for find_bydate function (works the same for find_bydescription and find_byamount)

![](/flowCharts/Find_ByDate.png)

## Record of Tasks
| Task No | Planned Action           | Planned Outcome                                                                          | Time estimate | Target completion date | Criterion |
|---------|--------------------------|------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram    | To have a clear idea of the hardware and software requirements for the proposed solution | 10min         | Sep 8                  | B         |
| 2       | Create login system      | To have a flow diagram and the code for login                                            | 30min         | Sep 14                 | B, C      |
| 3       | Create filtration system | To have a functional system and flowchart for saving and filtering transactions          | 30min         | Sep 17                 | B, C      |
| 4       | Add and del tran.        | To have system to delete and add transactions for different users                        | 15min         | Sep 18                 | C         |
| 5       | Create colours           | To create system, that displays texts in terminal in different colours                   | 10min         | Sep 19                 | C         |
| 6       | Edit text visualisation  | To save all most of the texts into txt. files                                            | 15min         | Sep 20                 | C         |
| 7       | Add comments             | To have the code clearly commented                                                       | 20min         | Sep 25                 | C         |
| 8       | Correct mistakes         | To change the code based on the client feedback                                          | 40min         | Sep 30                 | A, C      |
| 9       | Develope documentaion    | To have a documentation, which clearly describes features and why they were used.        | 60min         | Oct 1                  | B, C      |
| 10      | Testing                  | To have a testing plan with tests made                                                   | 30min         | Oct 1                  | A         |
| 11      | Create Hash encoding     | To create system that protects password by hash encoding and salt                        | 30min         | Oct 2                  | B, C      |


## Testing Plan
| Test No | Type of test        | Area Tested               | Outcome of test                                                                                                | Time estimate | Target completion date | Criterion |
|---------|---------------------|---------------------------|----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Unit Testing        | Login System              | Confirmed that user can login and system gives him 3 attempts                                                  | 5min          | Sep 30                 | B         |
| 2       | Unit Testing        | Add/delete tran.          | Confirm that user can add/delete transaction and the json file is updated                                      | 5min          | Sep 30                 | B         |
| 3       | Unit Testing        | Balance viewer            | Confirm that balance displayed by programm is correct                                                          | 5min          | Sep 30                 | B         |
| 4       | Unit Testing        | Filtering tran.           | Confirm that the filtration of transaction based on different inputs works                                     | 5min          | Sep 30                 | B         |
| 5       | Unit Testing        | Different users           | Confirm that when signing with different username and password,  transactions also changes                     | 5min          | Sep 30                 | B         |
| 6       | Integration Testing | Add tran. and  view tran. | Confirm that the add transaction and viewing and filtering transactions  functions work well with one another. | 5min          | Sep 30                 | B         |
| 7       | System Testing      | General                   | Confirm that the system works as a whole                                                                       | 5min          | Sep 30                 | B         |
| 8       | Userbility Testing  | General                   | Confirming that the system is clear                                                                            | 5min          | Sep 30                 | B         |


# Criteria C: Development
All the functions are commented in the code in files operations.py and project.py

## Login System
My client requires a system to protect the private data. I thought about using a login system to accomplish this requirement using a if condition and the open command to work with a csv file. The csv file contains the username and password of the user. The code is the following:
```python
def try_login(username:str, password:str) -> bool:
    with open ("/Project/users.csv", "r") as f:
        data = f.readlines()
    for line in data: #checks if the username and password are in the csv file, therefore if the user exists
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
    result = try_login(input_username, input_password) #calls try_login function which check users first try to login
    while not result and attempts > 0: #gives user 3 attempts to login, calling try_login function again
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
    with open("Project/transactions.json", "r") as f: #opens the json file
        data = json.load(f) #uses json library to load the data
    dates = []
    amounts = []
    descriptions = []
    for tran in data[user]: #goes through the list of transactions of the user, which are saved in the dictionary under his username in the json file
        dates.append(tran["date"])
        amounts.append(tran["amount"])
        descriptions.append(tran["description"])
    return dates, amounts, descriptions #returns the lists of dates, amounts and descriptions

def add_transaction(date, amount, description, user):
    with open("Project/transactions.json", "r") as f:
        data = json.load(f)
    data[user].append({"date": date, "amount": amount, "description": description}) #adds the transaction to the list of transactions of the user, every transaction is a dictionary
    with open("Project/transactions.json", "w") as f:
        json.dump(data, f, indent=4) #saves the updated data in the json file

def Delete_Transaction(date, amount, description, user):
    with open("Project/transactions.json", "r") as f:
        data = json.load(f)
    deleted = False
    for tran in data[user]: #goes through the list of transactions of the user and deletes the transaction if it matches the input
        if tran["date"] == date and tran["amount"] == amount and tran["description"] == description:
            data[user].remove(tran)
            deleted = True
            colours.pGreen("Transaction deleted") #inform the user that the transaction was deleted
    if not deleted:
        colours.pRed("Transaction not found") #inform the user that the transaction was not found
    with open("Project/transactions.json", "w") as f:
        json.dump(data, f, indent=4) #saves the updated data in the json file
```
## Filtering transactions
My client requires a system to filter the transactions. I thought about using a function to filter the transactions by date, category or amount in certain range. Functions take as an input lists with dates, amounts and descriptions, which have been loaded earlier. Elements of specific transaction are saved under the same index in the lists. The code is the following:
```python
def Find_ByDate(dates, amounts, descriptions, date):
    """
    filters the transactions by date
    """
    ret_amounts = []
    ret_descriptions = []
    for i in range(len(dates)): #iterates through the dates
        if dates[i] == date: #if the date is the same as the date we are looking for, it adds the amount and description to the lists
            ret_amounts.append(amounts[i]) 
            ret_descriptions.append(descriptions[i])
    return ret_amounts, ret_descriptions #returns the lists


def Find_ByDescription(dates, amounts, descriptions, description):
    """
    filters the transactions by description
    """
    ret_dates = []
    ret_amounts = []
    for i in range(len(descriptions)): #iterates through the descriptions
        if descriptions[i] == description: #if the description is the same as the description we are looking for, it adds the date and amount to the lists
            ret_dates.append(dates[i])
            ret_amounts.append(amounts[i])
    return ret_dates, ret_amounts

def Find_ByAmount(dates, amounts, descriptions, minamount, maxamont):
    """
    filters the transactions by amount
    """
    ret_dates = []
    ret_descriptions = []
    ret_amounts = []
    for i in range(len(amounts)): #iterates through the amounts
        if int(amounts[i]) >= minamount and int(amounts[i]) <= maxamont: #if the amount is between the min and max amount, it adds the date, description and amount to the lists
            ret_dates.append(dates[i])
            ret_descriptions.append(descriptions[i])
            ret_amounts.append(amounts[i])
    return ret_dates, ret_descriptions, ret_amounts
```

## Viewing txt. files
My client requires a system with which he/she can interact and that requires some text visualisation. I thought about using a txt. file to accomplish this requirement, which would eventualy allow also translation into different languages. The txt. file contains the basic description of the cryptocurrency selected or from which client can choose. The code is the following:
```python
def print_text_file(filename:str):
    with open(filename, "r") as f:
        data = f.readlines()
    for line in data:
        print(line.strip())
```
## Running program
All the functions are called in the main function, which also takes care of most of the communication with the user. Most of the functions are called from the operations file , which handles most of the filtering and getting information from the json file. The code is the following:
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

# Video proof
Here is a video proof of the project: https://drive.google.com/file/d/1-G26xBxbfvCaeoeWtWYoHNuZr5njpXzD/view?usp=sharing


