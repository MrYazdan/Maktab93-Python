from admin.callbacks import login, register, logout
from core.router import Router, Route
from core.state import StateManager

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
            Route("Register Event", callback=None),
            Route("Reports", callback=None),
        ]),
        Route("Events", children=[
            Route("Buy Ticket", callback=None)
        ]),
        Route("Logout", callback=logout, condition=StateManager.get_user),
    ])
)
