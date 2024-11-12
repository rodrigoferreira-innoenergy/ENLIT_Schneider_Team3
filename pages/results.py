import dash
from dash import html
import dash_bootstrap_components as dbc

# Register the page with Dash
dash.register_page(__name__, path='/results')

# Layout for the results page
layout = dbc.Container([
    html.H1("Dashboard", style={'textAlign': 'center', 'fontWeight': 'bold'}),

    # Dark gray rectangle with the "Current Solution" button
    dbc.Row(
        dbc.Col(
            dbc.Button(
                "Current Solution",
                href="/dashboard",  # Redirect link
                color="dark",  # Button color
                style={
                    "height": "100px",
                    "background-color": "#d4d4d4",  # Dark gray color
                    "color": "white",  # Text color
                    "display": "flex",
                    "align-items": "center",
                    "justify-content": "center",
                    "font-size": "24px",
                    "font-weight": "bold",
                    "border-radius": "8px",  # Rounded corners
                    "width": "100%"  # Full width of the column
                }
            ),
            width=12  # Full width
        ),
        className="mb-4"  # Margin below the rectangle
    ),

    # Row for the "Custom Solution" button
    dbc.Row(
        dbc.Col(
            dbc.Button(
                "Custom Solution",
                href="/custom",  # Redirect link
                color="info",  # Button color
                style={
                    "height": "100px",
                    "background-color": "#17a2b8",  # Info color (light blue)
                    "color": "white",  # Text color
                    "display": "flex",
                    "align-items": "center",
                    "justify-content": "center",
                    "font-size": "18px",
                    "font-weight": "bold",
                    "border-radius": "8px",  # Rounded corners
                    "width": "100%"  # Full width of the column
                }
            ),
            width=12  # Full width
        ),
        className="mb-4"  # Margin below the button
    ),

    # Row for three vertical rectangles with buttons
    dbc.Row([
        # First button for "Cost Saving"
        dbc.Col(
            dbc.Button(
                [
                    html.Div("Cost Saving", style={'fontSize': '20px', 'margin': '0'}),  # Increased size
                    html.Div("Total Cost: 655776.82€", style={'margin': '0'}),
                    html.Div("Cost per MWh: 77.85€", style={'margin': '0'}),
                    html.Div("Emissions: 157.42 kg/MWh", style={'margin': '0'}),
                    html.Div("Risk: High exposure to grid volatility", style={'margin': '0'}),
                ],
                href="/lowcost",  # Redirect link
                color="success",  # Button color
                style={
                    "height": "300px",
                    "background-color": "#7AC943",  # Green color
                    "color": "white",  # Text color
                    "font-size": "14px",
                    "font-weight": "bold",
                    "border-radius": "8px",
                    "width": "100%",
                    "display": "flex",
                    "flex-direction": "column",  # Stack items vertically
                    "align-items": "center",
                    "justify-content": "center",
                    "textAlign": "center"  # Center align the text
                }
            ),
            width=4  # Each takes one-third of the row
        ),

        # Second button for "Reduced CO2 Emissions"
        dbc.Col(
            dbc.Button(
                [
                    html.Div("Reduced CO2 Emissions", style={'fontSize': '20px', 'margin': '0'}),  # Increased size
                    html.Div("Total Cost: 620000.00€", style={'margin': '0'}),
                    html.Div("Cost per MWh: 75.00€", style={'margin': '0'}),
                    html.Div("Emissions: 140.00 kg/MWh", style={'margin': '0'}),
                    html.Div("Risk: High exposure to renewable intermittency risk", style={'margin': '0'}),
                ],
                href="/lowco2",  # Redirect link
                color="success",  # Button color
                style={
                    "height": "300px",
                    "background-color": "#7AC943",  # Green color
                    "color": "white",  # Text color
                    "font-size": "14px",
                    "font-weight": "bold",
                    "border-radius": "8px",
                    "width": "100%",
                    "display": "flex",
                    "flex-direction": "column",  # Stack items vertically
                    "align-items": "center",
                    "justify-content": "center",
                    "textAlign": "center"  # Center align the text
                }
            ),
            width=4  # Each takes one-third of the row
        ),

        # Third button for "Low Risk"
        dbc.Col(
            dbc.Button(
                [
                    html.Div("Low Risk", style={'fontSize': '20px', 'margin': '0'}),  # Increased size
                    html.Div("Total Cost: 827161.22€", style={'margin': '0'}),
                    html.Div("Cost per MWh: 98.19€", style={'margin': '0'}),
                    html.Div("Emissions: 69.7 kg/MWh", style={'margin': '0'}),
                    html.Div("Risk: Minimum Risk", style={'margin': '0'}),
                ],
                href="/lowrisk",  # Redirect link
                color="success",  # Button color
                style={
                    "height": "300px",
                    "background-color": "#7AC943",  # Green color
                    "color": "white",  # Text color
                    "font-size": "14px",
                    "font-weight": "bold",
                    "border-radius": "8px",
                    "width": "100%",
                    "display": "flex",
                    "flex-direction": "column",  # Stack items vertically
                    "align-items": "center",
                    "justify-content": "center",
                    "textAlign": "center"  # Center align the text
                }
            ),
            width=4  # Each takes one-third of the row
        ),
    ],
    className="mb-4"  # Margin below the button row
    ),

    # Row for "Our Recommendation" button
    dbc.Row(
        dbc.Col(
            dbc.Button(
                "Our Recommendation",
                href="/bestscenario",  # Redirect link
                color="success",  # Button color
                style={
                    "height": "150px",
                    "background-color": "#019f4d",  # Green color
                    "color": "white",  # Text color
                    "display": "flex",
                    "align-items": "center",
                    "justify-content": "center",
                    "font-size": "24px",
                    "font-weight": "bold",
                    "border-radius": "8px",  # Rounded corners
                    "width": "100%"  # Full width of the column
                }
            ),
            width=12  # Full width
        ),
        # className="mb-4"  # Margin below the rectangle
    ),

], fluid=True)  # Make the container fluid
