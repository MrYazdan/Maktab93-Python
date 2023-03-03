from core.state import StateManager
from core.utils import banner


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

    def __init__(self, name, description=None, callback=None, children=None, condition=lambda: True):
        self.parent = None
        self.children = None

        self.name = name
        self.description = description
        self.callback = callback
        self.condition = condition

        # self._set_parent(children) if children else None
        children and self._set_parent(children)

    def _set_parent(self, children):
        for child in children:
            child.parent = self
        self.children = children

    def _get_route(self):
        try:
            banner(StateManager.get_current_route_name())
            print(self.description or "", end="\n\n")

            if children := [child for child in self.children if child.condition()]:
                for child in children:
                    print(f"\t{children.index(child) + 1}. {child.name}")
                print(f"\n\t0. " + ("Exit" if not self.parent else f"Back to {self.parent.name}"))

                index = int(input("\n> ")) - 1
                route = children[index] if index != -1 else self.parent

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
                route.callback and route.callback(route)
            except Exception as e:
                banner("Error")
            input("\nPress Enter to continue ... ")
            StateManager.delete_last_route_name()
            route.parent()


class Router:
    """
        routes
    """

    def __init__(self, route):
        self.route = route
        StateManager.add_route_name(route.name)

    def __call__(self, *args, **kwargs):
        self.route()

# from time import sleep
#
#
# class TimeLoop:
#     def __init__(self, timeout):
#         self.timeout = timeout
#         self.count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         print("Count of TimeLoop:", self.count)
#         sleep(self.timeout)
#         self()
#
#
# TimeLoop(1)()
