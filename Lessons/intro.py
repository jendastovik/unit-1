# documentation
"""
today we will use input output and functions
aug 23
"""


def quizz1(str1: str):
    spl = str1.split()
    final = ""
    for word in spl:
        if len(word) > 2:
            final += word[0] + str(len(word) - 2) + word[-1]
        else:
            final += word
        final += " "
    return final


def get_info():
    """
    gets the info from the user
    """
    FN = input("what is your first name? ")
    LN = input("what is your last name? ")
    yr = input("what year were you born? ")
    return FN, LN, yr

def validate(yr):
    """
    this function will validate the year
    """
    for i in range(20):
        try:
            yr = int(yr)
            break
        except ValueError:
            print("you have {20-i} tries left")
            yr = input("please enter a valid year ")
    return yr

def create_mail(FN, LN, yr):
    """
    creates the email fro uwc isak
    """
    yr = validate(yr)
    return(f"{yr}.{FN}.{LN}@uwcisak.jp")


#print(create_mail(*get_info()))

def capitalize(tx):
    tx = tx.title()
    return tx

def check_email(email):
    """
    checks if the email is valid
    """
    return "@uwcisak.jp" in email
        
