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