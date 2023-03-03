from core.utils import banner, try_again
from event.models import Event, Ticket


def show_event_and_buy_ticket(route):
    try:
        if events := Event.events():
            for event in events:
                print(f"\t{str(event)}")

            selected_id = int(input("\n\nPlease enter event id : "))

            event = Event.get_event_by_id(selected_id)
            assert event, "Event not found !"

            national_code = input("Please enter your national code : ")
            Ticket(national_code, event)

            # save changed in file db :
            Event.db.update(Event.events())

            print("\n\nYour Ticket has been successfully issued !")
        else:
            print("\nEmpty ! :(")
    except (Exception, KeyboardInterrupt, AssertionError) as e:
        banner("Error")
        print(e)

        # try | again !
        try_again(route, show_event_and_buy_ticket)
