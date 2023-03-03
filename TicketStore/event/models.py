from uuid import uuid4
from core.handlers import FileHandler


class Event:
    __db = FileHandler("storage/events.pickle")
    __events = __db.get_list_data

    @classmethod
    def get_event_by_id(cls, _id):
        for event in cls.__events():
            if event.id == _id:
                return event

    @classmethod
    def events(cls):
        return cls.__events()

    def __init__(self, name, capacity, date="2023-03-03"):
        self.date = date
        self.name = name

        self.__capacity = int(capacity)
        self.__reserved_count = 0

        self.__id = uuid4().clock_seq
        self.__class__.__db.append(self)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        assert isinstance(new_name, str) and 3 <= len(new_name) <= 32, "Name invalid"

        self.__name = new_name

    @property
    def remaining_capacity(self):
        return self.__capacity - self.__reserved_count

    def reserve(self):
        self.__reserved_count += ((self.__reserved_count + 1) <= self.__capacity)

    def __str__(self):
        return f"[Event:{self.id}] Name: {self.name}, Remaining Capacity: {self.remaining_capacity}"

    def __eq__(self, _event):
        return self.id == _event.id


class Ticket:
    __db = FileHandler("storage/tickets.pickle")
    __tickets = __db.get_list_data

    def __init__(self, national_code, event):
        assert event in Event.events(), "Event not found !"
        self.event = event

        self.national_code = national_code
        self.__id = uuid4().clock_seq

        self.event.reserve()
        self.__class__.__db.append(self)

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f"[T:{self.__id}][E:{self.event}][NC:{self.national_code}]"
