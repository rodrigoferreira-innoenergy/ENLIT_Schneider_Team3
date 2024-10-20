from dash import Dash, dcc
import dash_bootstrap_components as dbc
import dash

# Custom theme from Bootswatch (Solar theme)
SOLAR_BOOTSWATCH = "https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.1.3/solar/bootstrap.min.css"

app = Dash(__name__, use_pages=True,
           external_stylesheets=[SOLAR_BOOTSWATCH, dbc.icons.FONT_AWESOME],  # Use Solar theme
           suppress_callback_exceptions=True, prevent_initial_callbacks=True)

server = app.server

# Import custom components (footer and nav)
from assets.footer import _footer
from assets.nav import _nav

# App Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([_nav], width=2),  # Navigation column
        dbc.Col([dash.page_container], width=10)  # Main content area
    ]),
    dbc.Row([
        dbc.Col([], width=2),
        dbc.Col([_footer], width=10)  # Footer column
    ]),
    dcc.Store(id='browser-memo', data=dict(), storage_type='session')  # Store data in the session
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)

