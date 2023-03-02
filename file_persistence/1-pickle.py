import pickle
# from file_persistence.model import Event


# with open("events.pickle", "rb") as f:
#     events = pickle.load(f)
#
# print(events)
#
# for event in events:
#     print(event.name)

# tehran = Event("Tehran", 50)
# isfahan = Event("Isfahan", 40)
# mashhad = Event("Mashhad", 40)
# shiraz = Event("Shiraz", 40)

# tehran_byte_str = pickle.dumps(tehran)
# tehran_from_pickle = pickle.loads(tehran_byte_str)
# print(tehran_from_pickle.name)
# print(tehran_from_pickle.id)
# print(tehran_from_pickle.remaining_capacity)

# with open("events.pickle", "ab") as f:
#     pickle.dump(Event.events(), file=f)

class Human:
    humans = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.__class__.humans.append(self)

    def __str__(self):
        return f"Name: '{self.name}', Age: '{self.age}'"


Human("Ali", 24)
Human("Fatemeh", 23)
Human("Akbar", 43)
Human("Zahra", 47)

with open("humans.pickle", "wb") as f:
    pickle.dump(Human.humans, file=f)
