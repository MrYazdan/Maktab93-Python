from admin.models import User


class StateManager:
    __routes = []
    __user = None

    @classmethod
    def logout(cls):
        cls.__user = None

    @classmethod
    def set_user(cls, user):
        assert isinstance(user, User), "User invalid"
        cls.__user = user

    @classmethod
    def get_user(cls):
        return cls.__user

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
