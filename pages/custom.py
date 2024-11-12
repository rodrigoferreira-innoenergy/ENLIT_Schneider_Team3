import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Register this page to be part of the multi-page app
dash.register_page(__name__, path='/custom')

# Load the CSV file
df = pd.read_csv('assets/df_final_emissions.csv', parse_dates=['datetime'])

# Melt the dataframe to long format with updated variable names
df_long = df.melt(id_vars=['datetime'], 
                  value_vars=['SITE CONSUMPTION Grid supply', 'SITE CONSUMPTION Natural Gas', 
                               'ONSITE SOLAR SYSTEM PRODUCTION', 'GRID Price', 
                               'NG Price', 'grid_consumption', 'solar_consumption', 
                               'wind_consumption', 'wind_excess', 'wind_total_consumption'],
                  var_name='Energy Type', 
                  value_name='Energy (kWh)')

# Layout for the custom scenario page
layout = dbc.Container([
    html.H1("Custom Scenario", style={'textAlign': 'center', 'fontWeight': 'bold'}),

    # Light gray horizontal rectangle with the title
    dbc.Row(
        dbc.Col(
            html.Div(
                "Cost, Emissions, and Risk",
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
    ),

    # Row with two sliders side by side
    dbc.Row(
        [
            # Column for the Priorities slider (left side)
            dbc.Col(
                html.Div(
                    children=[
                        html.Div(
                            style={
                                "height": "50px",
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
                        # Additional information
                        html.Div(
                            [
                                html.Span("Total Cost: ", style={'fontWeight': 'bold'}),
                                "839222.23  |  ",
                                html.Span("Cost per MWh: ", style={'fontWeight': 'bold'}),
                                "99.60€  |  ",
                                html.Span("Emissions: ", style={'fontWeight': 'bold'}),
                                "11.8 kg/MWh  |  ",
                                html.Span("Risk: ", style={'fontWeight': 'bold'}),
                                "High exposure to renewable intermittency risk",
                            ],
                            style={
                                "textAlign": "center",
                                "fontSize": "20px",
                                "padding": "10px",
                                "background-color": "#f0f0f0",  # Light gray color
                                "border-radius": "8px"  # Rounded corners
                            }
                        )
                    ]
                ),
                width=12  # Full width
            ),

            # Column for the Risk Level slider (right side)
            dbc.Col(
                html.Div([
                    html.Label("Risk Level:", 
                               style={"fontWeight": "bold", "display": "block", "textAlign": "center"}),
                    dcc.Slider(
                        id='risk-slider',
                        min=1,
                        max=3,
                        step=1,
                        marks={1: 'Low', 2: 'Medium', 3: 'High'},
                        value=2,
                        tooltip={"placement": "bottom", "always_visible": True},
                        vertical=False
                    )
                ]),
                width=6  # Half width of the row
            )
        ],
        className="mb-4"  # Margin below the sliders
    ),

    # Lock button
    dbc.Row(
        dbc.Col(
            html.Div(
                dbc.Button(
                    "Lock Choices", 
                    id="lock-button", 
                    color="primary", 
                    style={"width": "100%", "fontWeight": "bold"}  # Full width button
                ),
                style={"textAlign": "center"}  # Center the button
            ),
            width=6,  # Make the button smaller
            lg={"size": 4, "offset": 4}  # Adjust for larger screens (centered)
        ),
        className="mb-4"  # Margin below the button
    ),

    # Date Picker
    dcc.DatePickerRange(
        id='date-picker-range-emissions',  # Updated ID
        display_format='YYYY-MM-DD',
        min_date_allowed=df['datetime'].min().date(),
        max_date_allowed=df['datetime'].max().date(),
        start_date=df['datetime'].min().date(),
        end_date=df['datetime'].max().date(),
        style={'padding': '5px'}
    ),

    # Dropdown for energy types
    dcc.Dropdown(
        id='energy-type-dropdown-emissions',  # Updated ID
        options=[
            {'label': 'Site Consumption Grid Supply', 'value': 'SITE CONSUMPTION Grid supply'},
            {'label': 'Site Consumption Natural Gas', 'value': 'SITE CONSUMPTION Natural Gas'},
            {'label': 'Onsite Solar Production', 'value': 'ONSITE SOLAR SYSTEM PRODUCTION'},
            {'label': 'Grid Price', 'value': 'GRID Price'},
            {'label': 'NG Price', 'value': 'NG Price'},
            {'label': 'Grid Consumption', 'value': 'grid_consumption'},
            {'label': 'Solar Consumption', 'value': 'solar_consumption'},
            {'label': 'Wind Consumption', 'value': 'wind_consumption'},
            {'label': 'Wind Excess', 'value': 'wind_excess'},
            {'label': 'Wind Total Consumption', 'value': 'wind_total_consumption'},
        ],
        value=['SITE CONSUMPTION Grid supply'],  # Default selected value
        multi=True,  # Allow multiple selections
        style={'color': 'black'}
    ),

    # Button to plot the graph
    dbc.Button("Plot Emissions Data", id='plot-button-emissions', color='primary', className='mb-3'),  # Updated ID

    # Graph
    dcc.Graph(id='energy-graph-emissions'),  # Updated ID
], fluid=True)

# Callback for plotting the graph
@dash.callback(
    Output('energy-graph-emissions', 'figure'),  # Updated ID
    Input('plot-button-emissions', 'n_clicks'),  # Updated ID
    State('date-picker-range-emissions', 'start_date'),  # Updated ID
    State('date-picker-range-emissions', 'end_date'),  # Updated ID
    State('energy-type-dropdown-emissions', 'value')  # Updated ID
)
def update_graph(n_clicks, start_date, end_date, selected_energy_types):
    if n_clicks is None:
        return px.line(title='Select a date range and variable to plot')  # Return empty graph if no clicks

    # Filter dataframe based on selected date range
    filtered_df = df_long[
        (df_long['datetime'] >= start_date) & (df_long['datetime'] <= end_date) & 
        (df_long['Energy Type'].isin(selected_energy_types))
    ]

    # Create the Plotly line plot
    fig = px.line(
        filtered_df, 
        x='datetime', 
        y='Energy (kWh)', 
        color='Energy Type',  
        labels={'Energy (kWh)': 'Energy (kWh)', 'datetime': 'Date'}
    )

    # Customize the layout of the plot
    fig.update_layout(
        yaxis_title='Energy (kWh)',
        xaxis_title='Date',
        legend_title_text='Energy Types',
        template='plotly_white',
        margin=dict(l=0, r=0, t=0, b=50)
    )

    return fig
