import time
import os


#st = "fjld"
#print(st)
#time.sleep(2)
#os.system('cls')

def checkPassword():
    with open("Lessons/ps.txt", "r") as inp:
        password = inp.readline()
    tr = ""
    while tr != password:
        tr = input("enter password: ")
    print("correct password")


checkPassword()
# menu
items = ["p1", "p2", "p3", "p4", "p5"]
prices = [10, 20, 30, 40, 50]

print("menu".center(50, " "))
for i in range(len(items)):
    print(f"{i+1}. {items[i].title().ljust(50, '.')}jp{prices[i]}")

order = {}

con = True

while con:
    n = input(f"please enter an item (1-{len(items)}): ")
    while not (n.isdigit() and n in [str(p) for p in range(1, len(items)+1)]):
        n = input(f"error, please enter an item (1-{len(items)}): ")
    if n not in order.keys(): order[int(n)] = 1
    else: order[int(n)] += 1
    for it in order.keys():
        print(f"{items[it].title().ljust(20, ' ')}x{order[it]} => jp{prices[it]*order[it]}")
    con = input("do you want to continue? (y/n): ").lower() == "y"

price = 0
for it in order.keys():
    price += prices[it]

#print(str(price).center(50, '-'))

import random
def rand():
    con = True
    times = 0
    while con:
        n = random.randint(1, 100)
        times += 1
        if n <= 15:
            con = False
    return times





