import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import os

# Register this page to be part of the multi-page app
dash.register_page(__name__)

# Load CSV files from the assets folder
df_consumption = pd.read_csv('assets/df_Consumption.csv')
df_hourly_data = pd.read_csv('assets/df_Hourly_Data.csv')

# Convert 'Date' columns to datetime
df_consumption['Date'] = pd.to_datetime(df_consumption['Date'])
df_consumption = df_consumption.sort_values(by='Date')
df_hourly_data['Date'] = pd.to_datetime(df_hourly_data['Date'])

# Get the date range for the date picker
min_date_consumption = df_consumption['Date'].min().date()
max_date_consumption = df_consumption['Date'].max().date()
min_date_hourly = df_hourly_data['Date'].min().date()
max_date_hourly = df_hourly_data['Date'].max().date()

# Page layout
layout = dbc.Container([
    
    html.H1("Dashboard", style={'textAlign': 'center', 'fontWeight': 'bold'}),
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
    ),

    # Button to plot the graphs
    dbc.Button("Plot Data", id='plot-button', color='primary', className='mb-3'),

    # df_Consumption
    html.H3("Site Consumption", style={'color': '#7AC943'}),
    dcc.DatePickerRange(
        id='date-picker-range-consumption',
        display_format='YYYY-MM-DD',
        min_date_allowed=min_date_consumption,
        max_date_allowed=max_date_consumption,
        start_date=min_date_consumption,
        end_date=max_date_consumption,
        style={
            'backgroundColor': '##fafafa',
            'color': '#7AC943',
            'border': '1px solid #7AC943',
            'padding': '5px'
        }  # Dark theme for date picker
    ),
    dcc.Graph(id='consumption-graph'),

    # df_Hourly Data
    html.H3("Hourly Data", style={'color': '#7AC943'}),
    dcc.DatePickerRange(
        id='date-picker-range-hourly',
        display_format='YYYY-MM-DD',
        min_date_allowed=min_date_hourly,
        max_date_allowed=max_date_hourly,
        start_date=min_date_hourly,
        end_date=max_date_hourly,
        style={
            'backgroundColor': '#333333',
            'color': '#7AC943',
            'border': '1px solid #7AC943',
            'padding': '5px'
        }  # Dark theme for date picker
    ),
    dcc.Graph(id='hourly-data-graph'),
])

# Callback for plotting both graphs
@dash.callback(
    Output('consumption-graph', 'figure'),
    Output('hourly-data-graph', 'figure'),
    Input('plot-button', 'n_clicks'),
    State('date-picker-range-consumption', 'start_date'),
    State('date-picker-range-consumption', 'end_date'),
    State('date-picker-range-hourly', 'start_date'),
    State('date-picker-range-hourly', 'end_date')
)
def update_graphs(n_clicks, start_date_consumption, end_date_consumption, start_date_hourly, end_date_hourly):
    # Initialize figures
    consumption_fig = {}
    hourly_data_fig = {}

    # Check if button is pressed
    if n_clicks is None:
        return consumption_fig, hourly_data_fig

    # Filter df_Consumption by selected date range
    filtered_df_consumption = df_consumption[(df_consumption['Date'] >= start_date_consumption) & 
                                             (df_consumption['Date'] <= end_date_consumption)]

    # Filter df_Hourly_Data by selected date range
    filtered_df_hourly_data = df_hourly_data[(df_hourly_data['Date'] >= start_date_hourly) & 
                                             (df_hourly_data['Date'] <= end_date_hourly)]

    # Common layout for dark mode with green accents
    dark_layout = {
        'paper_bgcolor': '#fafafa',  # Dark background for the graph
        'plot_bgcolor': '#fafafa',   # Dark plot area background
        'font': {'color': '#7AC943'},  # Schneider Electric green for text
        'xaxis': {
            'showgrid': False,
            'color': '#7AC943',  # Green for axes
            'tickcolor': '#7AC943',  # Green for ticks
        },
        'yaxis': {
            'showgrid': False,
            'color': '#7AC943',  # Green for axes
            'tickcolor': '#7AC943',  # Green for ticks
        }
    }

    # Create Plotly graph for df_Consumption with gray line
    consumption_fig = px.line(filtered_df_consumption, x='Date', y='SITE CONSUMPTION (kWh/yr)', title='Site Consumption Over Time')
    consumption_fig.update_layout(**dark_layout)
    consumption_fig.update_traces(line=dict(color='#B0B0B0'))  # Gray line

    # Create Plotly graph for df_Hourly_Data with gray line
    hourly_data_fig = px.line(filtered_df_hourly_data, x='Date', y='SITE CONSUMPTION Grid supply (kWh)', title='Hourly Data - Grid Supply')
    hourly_data_fig.update_layout(**dark_layout)
    hourly_data_fig.update_traces(line=dict(color='#B0B0B0'))  # Gray line

    return consumption_fig, hourly_data_fig
