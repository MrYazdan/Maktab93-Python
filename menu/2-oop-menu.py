from os import system as terminal, name as os_name


def say_hello():
    print("Hi, what's up honey :)")


def say_goodbye():
    print("Hi, what's up honey :)")


def clear() -> None:
    terminal("cls" if os_name.lower() == "nt" else "clear")


def banner(name: str) -> None:
    clear()
    print("=" * 52, name.title().center(52), "=" * 52, sep="\n")


class StateManager:
    __routes = []

    @classmethod
    def get_current_route_name(cls):
        return " > ".join(cls.__routes)

    @classmethod
    def add_route_name(cls, name):
        if not len(cls.__routes) or cls.__routes[-1] != name:
            cls.__routes.append(name)

    @classmethod
    def delete_last_route_name(cls) -> None:
        cls.__routes.pop()


class CallBack:
    """
        function
    """

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.func()


class Route:
    """
        name
        callback
        description
        epilog
        parent
        condition
        children
    """

    def __init__(self, name, description=None, callback=None, children=None):
        self.parent = None
        self.children = None

        self.name = name
        self.description = description
        self.callback = callback

        # self._set_parent(children) if children else None
        children and self._set_parent(children)

    def _set_parent(self, children):
        for child in children:
            child.parent = self
        self.children = children

    def _get_route(self):
        try:
            banner(StateManager.get_current_route_name())
            print(self.description or "", end="\n")

            if self.children:
                for child in self.children:
                    print(f"\t{self.children.index(child) + 1}. {child.name}")
                print(f"\n\t0. " + ("Exit" if not self.parent else f"Back to {self.parent.name}"))

                index = int(input("\n> ")) - 1
                route = self.children[index] if index != -1 else self.parent

                if not route:
                    banner("Exit")

                    if input("Do you want to exit ? [y|N] ").strip().lower()[0] == "y":
                        print("Goodbye !")
                        exit()
                    else:
                        self()
                return route
            else:
                return self
        except (IndexError, ValueError, KeyboardInterrupt):
            banner("Error")
            input("Please enter a valid item\n\nPress Enter to continue ... ")
            self()

    def __call__(self, *args, **kwargs):
        StateManager.add_route_name(self.name)

        route = self._get_route()

        if self.parent == route:
            StateManager.delete_last_route_name()
            route()
        elif route.children:
            route()
        else:
            try:
                banner(route.name)
                route.callback and route.callback()
            except Exception as e:
                banner("Error")
            input("\nPress Enter to continue ... ")
            StateManager.delete_last_route_name()
            route.parent()


class Router:
    """
        routes
    """

    def __init__(self, route: Route):
        self.route = route
        StateManager.add_route_name(route.name)

    def __call__(self, *args, **kwargs):
        self.route()


router = Router(
    Route("Main", children=[
        Route("Say hello First", callback=say_hello),
        Route("Say hello 2", callback=say_hello),
        Route("Say hello 3", callback=say_hello),
        Route("Goodbye menu", children=[
            Route("Say bye 1", callback=say_goodbye),
            Route("Say bye 2", callback=say_goodbye),
            Route("Say bye 3", callback=say_goodbye),
            Route("Goodbye menu", children=[
                Route("Say bye 1", callback=say_goodbye),
                Route("Say bye 2", callback=say_goodbye),
                Route("Say bye 3", callback=say_goodbye),
            ]),
        ]),
        Route("Say Goodbye", children=[
            Route("Say hello 1", callback=say_hello),
            Route("Say hello 2", callback=say_hello),
            Route("Say hello 3", callback=say_hello),
        ])
    ])
)

router()
