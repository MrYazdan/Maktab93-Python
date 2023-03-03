from getpass import getpass

from admin.models import User
from core.state import StateManager
from core.utils import banner, try_again
from event.models import Event


def login(route):
    try:
        username = input("Please enter your username: ").strip().lower()
        assert username, "Username should not be empty !"

        password = getpass("Please enter your password: ")
        assert password, "Password should not be empty !"

        user = User.authentication(username, password)
        assert user, "User not found !"

        StateManager.set_user(user)

        print("\n- Login successful ✅")
        print(f"\n- Welcome {user.username}")
    except (Exception, KeyboardInterrupt, AssertionError) as e:
        banner("Error")
        print(e)

        # try | again !
        try_again(route, login)


def register(route):
    try:
        username = input("Please enter your username: ").strip().lower()
        assert username, "Username should not be empty !"

        password = getpass("Please enter your password: ")
        assert password, "Password should not be empty !"

        confirm_password = getpass("Please enter confirm password: ")
        assert confirm_password, "Confirm password should not be empty !"
        assert confirm_password == password, "Confirm password and password does not match !"

        user = User(username, password)
        assert user, "User not found !"

        print("\n- Register successful ✅")
    except (Exception, KeyboardInterrupt, AssertionError) as e:
        banner("Error")
        print(e)

        # try | again !
        try_again(route, register)


def logout(route):
    StateManager.logout()
    print("\n- Logout successful ✅")


def register_event(route):
    try:
        name = input("Please enter event name: ").title()
        assert name, "Name should not be empty !"

        capacity = input("Please enter event capacity: ")
        assert capacity, "Capacity should not be empty !"
        assert capacity.isnumeric(), "Capacity should be numeric !"

        date = input("Please enter event Date: ")

        Event(name, capacity, date or "2023-03-03")

        print("\n- Register event successful ✅")
    except (Exception, KeyboardInterrupt, AssertionError) as e:
        banner("Error")
        print(e)

        # try | again !
        try_again(route, register)
