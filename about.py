import dash
from dash import html


dash.register_page(__name__, path='/about')

layout = html.Div([
    html.H1("ENLIT Schneider Electric Challenge - Team 3"),

    html.P("Names of the members")
])
