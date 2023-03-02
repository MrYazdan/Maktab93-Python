class Event:
    __objects = []
    """
        name : str
        capacity : int
        remaining_capacity : int
        date : "2-3-2023"
    """

    def __new__(cls, *args, **kwargs):
        for o in cls.__objects:
            if o.name == args[0]:
                return False

        return super().__new__(cls)

    @classmethod
    def events(cls):
        return cls.__objects

    def __init__(self, name, capacity, date="2023"):
        self.date = date
        self.name = name

        self.__capacity = int(capacity)
        self.__reserved_count = 0

        self.__id = len(self.__class__.__objects)
        self.__class__.__objects.append(self)

    def file_format(self):
        return f"{self.name}|{self.remaining_capacity}|{self.date}"

    @classmethod
    def create_event_from_file_format(cls, row):
        return cls(*row.strip().split("|"))

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        # if isinstance(new_name, str) and 3 <= len(new_name) <= 32:
        #     self.__name = new_name
        # raise ValueError
        assert isinstance(new_name, str) and 3 <= len(new_name) <= 32, \
            "Name invalid"

        self.__name = new_name

    @property
    def remaining_capacity(self):
        return self.__capacity - self.__reserved_count

    def reserve(self):
        # 1:
        # if self.__reserved_count + 1 <= self.__capacity:
        #     self.__reserved_count += 1
        # 2:
        # self.__reserved_count += 1 if self.__reserved_count + 1 <= self.__capacity else 0
        # 3:
        # a, b = 10, 20
        # a += a < b
        # b += a > b
        # print(a, b)
        self.__reserved_count += ((self.__reserved_count + 1) <= self.__capacity)

    # def __repr__(self):
    #     print("repr called")
    #     return "From repr method"

    def __str__(self):
        return f"Name: {self.name}, Capacity: {self.__capacity}"
        # print("Str method - before super")
        # return super(Event, self).__str__()
        # super(Event, self).__str__()
        # print("Str method - after super")
        # return "From str method"

    def __eq__(self, _event):
        return self.id == _event.id


# load from file:
with open("events.data", "a+") as f:
    f.seek(0)
    for line in f.readlines():
        Event.create_event_from_file_format(line)

# print(*Event.events(), sep="\n")
tehran = Event("Tehran", 40)
isfahan = Event("Isfahan", 40)
mashhad = Event("Mashhad", 40)
shiraz = Event("Shiraz", 40)

# save in file:
with open("events.data", "w") as f:
    for event in Event.events():
        print(event.file_format(), file=f)
