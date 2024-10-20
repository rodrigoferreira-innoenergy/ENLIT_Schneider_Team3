import dash
from dash import html


dash.register_page(__name__, path='/contact')

layout = html.Div([
    html.H1("Contact Us"),
    html.P("You can contact us at example@example.com."),
    html.P("Phone: +123456789")
])
