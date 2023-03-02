from os import system as terminal, name as os_name


def clear():
    terminal("clear" if os_name.lower() != "nt" else "cls")


def say_hello():
    print("Hi, what's up honey :)")


def say_goodbye():
    print("Hi, what's up honey :)")


# Dict routing
# tuple( title, callback|'back' )
# dict{
#       title: "str"
#       , 0 ... n : tuple, dict
#       }


main_routes = {
    1: ("Say hello to you", say_hello),
    2: {
        "title": "Child Menu",
        1: ("Child say hello", say_hello),
        2: {
            "title": "Grand Child Menu",
            1: ("Child say hello", say_hello),
            0: ("Back to parent menu", "back")
        },
        0: ("Back to parent menu", "back")
    },
    0: ("Exit", exit)
}


def router(routes, parent=None):
    clear()

    for index, route in routes.items():
        if isinstance(route, tuple):
            print(f"{index}. {route[0]}")
        elif isinstance(route, dict):
            print(f"{index}. {route['title']}")

    prompt = int(input("\n> "))

    if isinstance(routes[prompt], tuple):
        if routes[prompt][1] == "back":
            router(parent, parent=routes)
        else:
            routes[prompt][1]()
            input("Press Enter to continue ...")
            router(routes)

    elif isinstance(routes[prompt], dict):
        router(routes[prompt], parent=routes)


router(main_routes)
