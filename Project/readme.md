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

Justify the tools/structure of your solution

## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the cyrptocurrency selected.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The electronic ledger allows to display the current balance.
5. The electronic ledger allows to display the transaction history, which can be filtred by date or category.
6. The elctronic ladger is protected by password and hash function.

# Criteria B: Design

## System Diagram

## Flow Diagrams


## Record of Tasks
|   | Task No | Planned Action        | Planned |   | Task No | Planned Action        | Planned Outcome                                                                          | Time estimate | Target completion date | Criterion |   |
|---|---------|-----------------------|------------------------------------------------------------------------------------------|---------------|------------------------|-----------|---|
|   | 1       | Create system diagram | To have a clear idea of the hardware and software requirements for the proposed solution | 10min         | Sep 24                 | B         |   |
|   | 2       | Create system diagram | To have a flow diagram and the code for the login system                                 | 30min         | Sep 14                 | B, C      |   |

# Criteria C: Development

## Login System
My client requires a system to protect the private data. I thought about using a login system to accomplish this requirement using a if condition and the open command to work with a csv file. More description of the code....
```.py
def simple_login(user:str, password:str)->bool:
    '''
    Simple authentication, needs fle user.csv
    :param user: string
    :param password: string
    :return: True/False if user is in database
    '''
    with open("user.csv") as file:
        database = file.readlines()
    output = False
    for line in database:
        line_cleaned = line.strip() #remove \n
        user_pass = line_cleaned.split(",")
        if user == user_pass[0] and password == user_pass[1]:
            output = True
            break

    return output


```
