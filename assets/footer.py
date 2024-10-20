import dash_bootstrap_components as dbc
from dash import html


_footer = dbc.Container(
    html.Footer(
        dbc.Row(
            dbc.Col(
                html.Div([
                    html.P("© 2024 Schneider Electric Challenge Team 3 | Smart Energy Strategy App", className="text-center"),
                    html.A("Privacy Policy", href="#", className="text-center")
                ], style={"padding": "10px"})
            )
        )
    ), fluid=True
)
