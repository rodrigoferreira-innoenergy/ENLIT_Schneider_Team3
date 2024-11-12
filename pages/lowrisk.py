import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Register this page to be part of the multi-page app
dash.register_page(__name__)

# Load the CSV file
df = pd.read_csv('assets/df_final_risk.csv', parse_dates=['datetime'])

# Melt the dataframe to long format
df_long = df.melt(id_vars=['datetime'], 
                  value_vars=['SITE CONSUMPTION Grid supply', 'SITE CONSUMPTION Natural Gas', 
                               'ONSITE SOLAR SYSTEM PRODUCTION', 'GRID Price', 
                               'NG Price', 'grid_consumption', 'solar_consumption', 
                               'wind_consumption', 'wind_excess'],
                  var_name='Energy Type', 
                  value_name='Energy (kWh)')
# Page layout
layout = dbc.Container([
    html.H1("Low Cost", style={'textAlign': 'center', 'fontWeight': 'bold'}),
    
    # Light gray horizontal rectangle with cost, emissions, and risk information
    dbc.Row(
        dbc.Col(
            html.Div(
                children=[
                    html.Div(
                        "Cost, Emissions and Risk",
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
                            "827161.22€  |  ",
                            html.Span("Cost per MWh: ", style={'fontWeight': 'bold'}),
                            "98.19€  |  ",
                            html.Span("Emissions: ", style={'fontWeight': 'bold'}),
                            "69.7 kg/MWh  |  ",
                            html.Span("Risk: ", style={'fontWeight': 'bold'}),
                            "Minimum Risk",
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
        className="mb-4"  # Margin below the rectangle
    ),

    # Date Picker
    dcc.DatePickerRange(
        id='date-picker-range-cost',  # Updated ID for date picker
        display_format='YYYY-MM-DD',
        min_date_allowed=df['datetime'].min().date(),
        max_date_allowed=df['datetime'].max().date(),
        start_date=df['datetime'].min().date(),
        end_date=df['datetime'].max().date(),
        style={'padding': '5px'}
    ),

    # Dropdown for energy types
    dcc.Dropdown(
        id='energy-type-dropdown-cost',  # Updated ID for dropdown
        options=[
            {'label': 'Onsite Solar Production', 'value': 'ONSITE SOLAR SYSTEM PRODUCTION'},
            {'label': 'Grid Consumption', 'value': 'GRID CONSUMPTION'},
            {'label': 'Site Consumption', 'value': 'SITE CONSUMPTION Grid supply'},
        ],
        value=['ONSITE SOLAR SYSTEM PRODUCTION'],  # Default selected value
        multi=True,  # Allow multiple selections
        style={'color': 'black'}
    ),

    # Button to plot the graph
    dbc.Button("Plot Data", id='plot-button-cost', color='primary', className='mb-3'),  # Updated ID for button

    # Graph
    dcc.Graph(id='energy-graph-cost'),  # Updated ID for graph
], fluid=True)

# Callback for plotting the graph
@dash.callback(
    Output('energy-graph-cost', 'figure'),  # Updated ID for graph output
    Input('plot-button-cost', 'n_clicks'),  # Updated ID for button input
    State('date-picker-range-cost', 'start_date'),  # Updated ID for start date
    State('date-picker-range-cost', 'end_date'),  # Updated ID for end date
    State('energy-type-dropdown-cost', 'value')  # Updated ID for dropdown value
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
