from file_persistence.model import Event

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
