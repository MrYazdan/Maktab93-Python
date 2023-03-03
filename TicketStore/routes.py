from admin.callbacks import login, register, logout, register_event
from core.router import Router, Route
from core.state import StateManager
from event.callbacks import show_event_and_buy_ticket

# Admin panel
#   Login Admin
#   Register Admin
#   --- ADMIN LOGGED IN ---
#   Logout
#   Register Event
#   Reports
# Events
#   Buy Ticket

router = Router(
    Route("Main", description="Ticket shop cli project", children=[
        Route("Login", callback=login, condition=lambda: not StateManager.get_user()),
        Route("Register", callback=register, condition=lambda: not StateManager.get_user()),
        Route("Admin Panel", condition=StateManager.get_user, children=[
            Route("Register Event", callback=register_event),
            Route("Reports", callback=None),
        ]),
        Route("Show Events | Buy Ticket", callback=show_event_and_buy_ticket),
        Route("Logout", callback=logout, condition=StateManager.get_user),
    ])
)
