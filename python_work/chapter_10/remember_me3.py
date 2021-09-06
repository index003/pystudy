import json


def get_stored_username():
    filename = 'username4.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What's your name?")
    filename = 'username4.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username.title()}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back,{username.title()}!")


greet_user()
