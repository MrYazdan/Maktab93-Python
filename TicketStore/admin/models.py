from core.handlers import FileHandler


class User:
    __db = FileHandler("storage/users.pickle")
    __users = __db.get_list_data

    @classmethod
    def authentication(cls, username, password):
        for user in cls.__users():
            if user.username == username and user.password == password:
                return user

    def __init__(self, username, password, first_name=None, last_name=None, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.password = password
        self.username = username

        self.__class__.__db.append(self)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_pass):
        # password validation
        self.__password = new_pass

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        # username validation
        # for user in self.__class__.__users:
        #     if user.username == new_username:
        #         raise ...
        # Generator =-> (for u in users if new_username == u.username)

        assert not any(user for user in self.__class__.__users() if user.username == new_username), \
            "Username exists !"
        self.__username = new_username
