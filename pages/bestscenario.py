import dash
from dash import html
import dash_bootstrap_components as dbc

# Register this page to be part of the multi-page app
dash.register_page(__name__, path='/bestscenario')

# Layout for the low CO2 emissions page
layout = dbc.Container([
    html.H1("Best Scenario", style={'textAlign': 'center', 'fontWeight': 'bold'}),

    # Light gray horizontal rectangle
    dbc.Row(
        dbc.Col(
            html.Div(
                "Cost, Emissions and Risk",
                style={
                    "height": "100px",
                    "background-color": "#f0f0f0",  # Light gray color
                    "color": "black",  # Text color
                    "display": "flex",
                    "align-items": "center",
                    "justify-content": "center",
                    "font-size": "24px",
                    "font-weight": "bold",
                    "border-radius": "8px"  # Rounded corners
                }
            ),
            width=12  # Full width
        ),
        className="mb-4"  # Margin below the rectangle
    )
], fluid=True)