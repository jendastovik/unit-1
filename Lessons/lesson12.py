def mystery(x, y):
    dif = x - y
    return (x*y + dif)

test_cases = [(2, 6), (4, 10), (10, 10), (70, 50)]
for (a, b) in test_cases:
    print(f"{a}, {b} ==> {mystery(a, b)}")

import json
def load_transactions():
    with open("Project/transactions.json", "r") as f:
        data = json.load(f)
    dates = []
    amounts = []
    descriptions = []
    for tran in data["transactions"]:
        dates.append(tran["date"])
        amounts.append(tran["amount"])
        descriptions.append(tran["description"])
        #print(f"{tran['date']}: {tran['amount']}, {tran['description']}")
    return dates, amounts, descriptions

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
    for i in range(len(amounts)):
        if amounts[i] >= minamount and amounts[i] <= maxamont:
            ret_dates.append(dates[i])
            ret_descriptions.append(descriptions[i])
    return ret_dates, ret_descriptions

def add_transaction(date, amount, description):
    with open("Project/transactions.json", "r") as f:
        data = json.load(f)
    data["transactions"].append({"date": date, "amount": amount, "description": description})
    with open("Project/transactions.json", "w") as f:
        json.dump(data, f, indent=4)

def Balance(amounts):
    total = 0
    for amount in amounts:
        total += int(amount)
    return total

def Delete_Transaction(date, amount, description, user):
    with open("Project/transactions.json", "r") as f:
        data = json.load(f)
    for tran in data[user]:
        if tran["date"] == date and tran["amount"] == amount and tran["description"] == description:
            data[user].remove(tran)
    with open("Project/transactions.json", "w") as f:
        json.dump(data, f, indent=4)