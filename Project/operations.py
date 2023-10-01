import json
import colours

def load_transactions(user:str):
    """
    loads the transactions of a user from the json file
    """
    with open("Project/transactions.json", "r") as f: #opens the json file
        data = json.load(f)
    dates = []
    amounts = []
    descriptions = []
    for tran in data[user]: #iterates through the transactions of the user
        dates.append(tran["date"]) #adds the date, amount and description to the lists
        amounts.append(tran["amount"])
        descriptions.append(tran["description"])
        #print(f"{tran['date']}: {tran['amount']}, {tran['description']}")
    return dates, amounts, descriptions

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
        if abs(int(amounts[i])) >= minamount and abs(int(amounts[i])) <= maxamont: #if the amount is between the min and max amount, it adds the date, description and amount to the lists
            ret_dates.append(dates[i])
            ret_descriptions.append(descriptions[i])
            ret_amounts.append(amounts[i])
    return ret_dates, ret_descriptions, ret_amounts

def add_transaction(date, amount, description, user):
    """
    opens the json file and adds a transaction to the list of transactions of a user
    """
    with open("Project/transactions.json", "r") as f: #opens the json file
        data = json.load(f) #loads the data from the json file
    data[user].append({"date": date, "amount": amount, "description": description}) #adds the transaction to the list of transactions of the user
    with open("Project/transactions.json", "w") as f: #opens the json file
        json.dump(data, f, indent=4) #saves the changes to the json file

def Balance(amounts):
    """
    calculates the balance of a user
    """
    total = 0
    for amount in amounts: #iterates through the amounts
        total += int(amount) #adds the amount to the total
    return total

def Delete_Transaction(date, amount, description, user):
    """
    deletes a transaction from the json file of a user
    """
    with open("Project/transactions.json", "r") as f: #opens the json file
        data = json.load(f) #loads the data from the json file
    deleted = False
    for tran in data[user]: #iterates through the transactions of the user
        if tran["date"] == date and tran["amount"] == amount and tran["description"] == description: #if the transaction is the same as the transaction we are looking for, it deletes it
            data[user].remove(tran)
            deleted = True
            colours.pGreen("Transaction deleted")
    if not deleted: #if the transaction was not found, it prints an error message
        colours.pRed("Transaction not found")
    with open("Project/transactions.json", "w") as f: #opens the json file
        json.dump(data, f, indent=4) #saves the changes to the json file
    