from dash import Dash, dcc
import dash_bootstrap_components as dbc
import dash

# Custom theme from Bootswatch
app = Dash(__name__, use_pages=True,
           external_stylesheets=[dbc.themes.DARKLY, dbc.icons.FONT_AWESOME, "/assets/custom_dark_style.css"],  
           suppress_callback_exceptions=True, 
           prevent_initial_callbacks=True)

server = app.server

# Import custom components (footer and nav)
from assets.footer import _footer
from assets.nav import _nav

# App Layout
app.layout = dbc.Container(id='app-container', children=[
    dbc.Row([
        dbc.Col([_nav], width=2),  # Navigation column
        dbc.Col([dash.page_container], width=10)  # Main content area
    ], className='flex-grow-1'),  # Allow this row to grow to fill space
    dbc.Row([
        dbc.Col([], width=2),
        dbc.Col([_footer], width=10)  # Footer column
    ]),
    dcc.Store(id='browser-memo', data=dict(), storage_type='session')  # Store data in the session
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
