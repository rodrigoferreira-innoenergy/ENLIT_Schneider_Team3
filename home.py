import dash
from dash import html


dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1("Smart Energy Strategy App"),
    html.P("Here it will be a description of the app"),
])
