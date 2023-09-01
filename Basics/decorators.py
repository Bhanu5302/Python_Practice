""" A decorator is a design pattern in Python that allows a user
to add new functionality to an existing object without modifying its structure"""

def login_required(f1):
    def inner(user, is_login):
        if is_login == False:
            print("Kindly login")
            return
        return f1(user, is_login)

    return inner


@login_required
def home(user, is_login):
    print(f"Successfully logged..! Welcome {user}")

home("Bhanu", True)
