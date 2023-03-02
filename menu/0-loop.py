from os import system as terminal, name as os_name

"""
 question ?

 1. ...
 2. ...

 0. Exit | Back

 >
"""


def clear():
    terminal("clear" if os_name.lower() != "nt" else "cls")


def say_hello():
    print("Hi, what's up honey :)")


def say_goodbye():
    print("Hi, what's up honey :)")


while True:
    clear()

    index = int(input("""
Welcome to main my cli

  1. Say hello
  2. Say Goodbye

  0. Exit

> """))

    if index == 1:
        say_hello()
    elif index == 2:
        say_goodbye()
    elif index == 0:
        exit()
    else:
        continue

    _ = input("Press Enter to back main :)")
