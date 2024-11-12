import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1("Smart Energy Strategy App", style={'textAlign': 'center', 'fontWeight': 'bold'}),
    html.P("Here it will be a description of the app", style={'textAlign': 'center', 'fontWeight': 'bold'}),
])
