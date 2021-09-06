def greet_user():
    print("Hello Function World!")


def greet_user2(username):
    print(f"Hello {username}!")


greet_user()
greet_user2('victor')


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print(f"\nPlease tell me your name: ")
    print("(Enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello {formatted_name}!")
