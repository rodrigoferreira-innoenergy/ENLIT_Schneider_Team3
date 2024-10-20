import dash_bootstrap_components as dbc

_nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", href="/", active="exact")),
        dbc.NavItem(dbc.NavLink("About", href="/about", active="exact")),
        dbc.NavItem(dbc.NavLink("Import", href="/import", active="exact")),
        dbc.NavItem(dbc.NavLink("Dashboard", href="/dashboard", active="exact")),
        dbc.NavItem(dbc.NavLink("Contact", href="/contact", active="exact")),
        
    ],
    vertical=True,  # Set the nav to be vertical for the sidebar
    pills=True,     # Highlight the active link with pills
)
