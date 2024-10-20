import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import os

# Register this page to be part of the multi-page app
dash.register_page(__name__)

# Page layout
layout = dbc.Container([
    html.H2("Imported Data Dashboards"),

    # Button to plot the graphs
    dbc.Button("Plot Data", id='plot-button', color='primary', className='mb-3'),

    # df_Consumption
    html.H3("Site Consumption"),
    dcc.DatePickerRange(
        id='date-picker-range-consumption',
        display_format='YYYY-MM-DD'
    ),
    dcc.Graph(id='consumption-graph'),

    # df_Hourly Data
    html.H3("Hourly Data"),
    dcc.DatePickerRange(
        id='date-picker-range-hourly',
        display_format='YYYY-MM-DD'
    ),
    dcc.Graph(id='hourly-data-graph'),
    
    dcc.Store(id='data-store')  # Store for DataFrames, same ID as in import.py
])

# Callback for plotting both graphs
@dash.callback(
    Output('consumption-graph', 'figure'),
    Output('hourly-data-graph', 'figure'),
    Input('plot-button', 'n_clicks'),
    Input('data-store', 'data'),  # Input from Store
    State('date-picker-range-consumption', 'start_date'),
    State('date-picker-range-consumption', 'end_date'),
    State('date-picker-range-hourly', 'start_date'),
    State('date-picker-range-hourly', 'end_date')
)
def update_graphs(n_clicks, data, start_date_consumption, end_date_consumption, start_date_hourly, end_date_hourly):
    # Initialize figures
    consumption_fig = {}
    hourly_data_fig = {}

    # Check if button is pressed
    if n_clicks is None or data is None:
        return consumption_fig, hourly_data_fig

    df_store = {key: pd.DataFrame(value) for key, value in data.items()}  # Convert back to DataFrames

    # Plot df_Consumption
    if 'df_Consumption' in df_store:
        df_consumption = df_store['df_Consumption']

        # Filter data by the selected date range
        if start_date_consumption and end_date_consumption:
            df_consumption = df_consumption[(df_consumption['Date'] >= start_date_consumption) & (df_consumption['Date'] <= end_date_consumption)]

        # Create Plotly graph
        consumption_fig = px.line(df_consumption, x='Date', y='SITE CONSUMPTION (kWh/yr)', title='Site Consumption Over Time')

    # Plot df_Hourly Data
    if 'df_Hourly Data' in df_store:
        df_hourly_data = df_store['df_Hourly_Data']

        # Filter data by the selected date range
        if start_date_hourly and end_date_hourly:
            df_hourly_data = df_hourly_data[(df_hourly_data['Date'] >= start_date_hourly) & (df_hourly_data['Date'] <= end_date_hourly)]

        # Create Plotly graph
        hourly_data_fig = px.line(df_hourly_data, x='Date', y='SITE CONSUMPTION Grid supply (kWh)', title='Hourly Data - Grid Supply')

    return consumption_fig, hourly_data_fig
