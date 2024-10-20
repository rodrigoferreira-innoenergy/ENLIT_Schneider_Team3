import dash
from dash import html, dcc, Input, Output, State, callback
import pandas as pd
import io
import base64
import json
import os


dash.register_page(__name__, path='/import')

layout = html.Div([
    html.H1("Importing your data"),
    html.P("Here you can import your Excel file: Data Base - Schneider Electric x InnoEnergy ENLIT Milan 2024"),
    
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False  # Only allow single file upload
    ),
    
    html.Div(id='output-data-upload'),
    
    # Button to save DataFrames
    html.Button('Save DataFrames', id='save-button', n_clicks=0),
    
    # Store for DataFrames
    dcc.Store(id='data-store')  
])

@callback(
    Output('output-data-upload', 'children'),
    Output('data-store', 'data'),  # Output to Store
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    State('upload-data', 'last_modified'),
    Input('save-button', 'n_clicks'),  # Added to detect button clicks
    prevent_initial_call=True  # Prevent callback firing on initial load
)
def parse_and_save_contents(contents, filename, date, save_button_clicks):
    if contents is None:
        return html.Div(["No file uploaded yet."]), None

    # Check if the uploaded file is an Excel file
    if not filename.endswith('.xls') and not filename.endswith('.xlsx'):
        return html.Div(["Invalid file type. Please upload an Excel file."]), None

    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    xls = pd.ExcelFile(io.BytesIO(decoded))
    
    # Extract all sheets except the "Site Information"
    sheet_names = [sheet for sheet in xls.sheet_names if sheet != "Site Information"]
    
    data_frames = {}
    output = []
    
    # Process the sheets and store them in a dictionary
    for sheet in sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet)
        
        # If there are "Month", "Day", and "Hour" columns, combine them into "Date" with year 2023
        if set(['Month', 'Day', 'Hour']).issubset(df.columns):
            df['Date'] = pd.to_datetime(
                {'year': 2023, 'month': df['Month'], 'day': df['Day'], 'hour': df['Hour']}
            )
            df = df.drop(columns=['Month', 'Day', 'Hour'])  # Drop the original columns
        
        # Convert Timestamps to strings for JSON serialization
        for col in df.select_dtypes(include=['datetime']).columns:
            df[col] = df[col].astype(str)  # Convert timestamps to strings
        
        # Store DataFrame as dictionary
        data_frames[f'df_{sheet}'] = df.to_dict(orient='records')  # Convert DataFrame to list of records for easier retrieval
        
        # Append the sheet name and the head of the DataFrame to the output
        output.append(html.H3(f"DataFrame name: df_{sheet}"))
        output.append(html.Pre(df.head().to_string(index=False)))  # Display the head of the DataFrame
    
    # If the save button has been clicked, save DataFrames as CSVs and return the stored data
    if save_button_clicks > 0:
        # Ensure the assets directory exists
        if not os.path.exists('assets'):
            os.makedirs('assets')
        
        # Save each DataFrame to CSV in the assets folder
        for sheet in sheet_names:
            df.to_csv(f'assets/df_{sheet}.csv', index=False)  # Save DataFrame as CSV
        
        return output, json.dumps(data_frames)  # Return the stored DataFrames as JSON string
    
    return output, dash.no_update  # Return output without updating data-store if button hasn't been clicked
