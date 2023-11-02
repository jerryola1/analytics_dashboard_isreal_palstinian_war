from dash import html
from dash import dcc
import dash
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
import re
from collections import Counter

external_stylesheets = [
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']


# Load the data into a DataFrame
file_path = 'Updated_Combined_BBNaijaAllStars_2023_Data.xlsx'  # Update this path
df = pd.read_excel(file_path)
data = pd.read_csv('bbnaijaCombined.csv')

# Inspect the first few rows of the DataFrame
print(data.head())
print(df.head())

df.drop(['Binders', 'User_y'], axis=1, inplace=True)


# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <!-- Other head content -->
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''


# Define primary colors
primary_colors = {'background': '#2171b5', 'text': '#fd8d3c'}

unique_usernames = data['tweets_username'].unique()
username_options = [{'label': username, 'value': username}
                    for username in unique_usernames]

time_range_options = [
    {'label': 'Last 7 Days', 'value': '7d'},
    {'label': 'Last 30 Days', 'value': '30d'},
    {'label': 'Last 3 Months', 'value': '3m'},
    # Add more as needed
]


# Define the app layout
app.layout = html.Div(className='container alert alert-primary', style={'backgroundColor': primary_colors['background'], 'textAlign': 'center'}, children=[

    # Header Row 1
    html.Div([
        html.H1("BBNaija Reality TV Show Dashboard", style={
                'color': primary_colors['text'], 'textAlign': 'center'})
    ], className="py-3", style={'gridColumn': 'span 12'}),

    # Filter Row 2
    html.Div(className='row py-3 justify-content-center', children=[
        html.Div(
            dcc.Dropdown(
                id='username-dropdown',
                options=username_options,
                style={'minWidth': '200px', 'maxWidth': '250px'}
            ),
            className='col-12 col-md-4 my-1',
            # style={'marginLeft': 'auto', 'marginRight': 'auto'}
        ),
        
        
        # html.Div(dcc.Dropdown(
        #     id='time-dropdown',
        #     options=time_range_options,
        #     style={'minWidth': '200px', 'maxWidth': '250px'}
        # ),
        #     className='col-sm-3 col-md-4 my-1'
        # ),
        
        html.Div(
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date='2023-10-01',
        end_date='2023-10-31',
        display_format='YYYY-MM-DD'
    ),
    className='col-sm-2 col-md-4 my-1'
),


        html.Div(dcc.Dropdown(
            id='hashtag-dropdown',
            options=time_range_options,
            style={'minWidth': '200px', 'maxWidth': '250px'}
        ),
            className='col-sm-3 col-md-4 my-1'
        ),

        # html.Div(dcc.Dropdown(
        #     id='sentiment-dropdown',
        #     options=time_range_options,
        #     style={'minWidth': '200px', 'maxWidth': '250px'}
        # ),
        #     className='col-sm-3 my-1'
        # ),
    ]),



    # # Overview Metrics Row 3
    # html.Div(className='row py-3 mb-3 bg-warning shadow rounded', children=[
    #     html.Div(id='total-tweets', className='col-4 text-center'),
    #     html.Div(id='unique-contributors', className='col-4'),
    #     html.Div(id='avg-likes', className='col-4')
    #     # html.Div(id='avg-retweets', className='col-3')
    # ]),


    # Overview Metrics Row 3
    html.Div(
        className='row py-3 mb-3 text-warning shadow-sm rounded',
        children=[
            html.Div(
                id='total-tweets',
                className='col text-center p-3 mb-5  rounded',
                children=[
                    # Your pie chart or other chart components go here
                ]
            ),
            html.Div(
                id='pie-chart',
                className='col text-center p-3 mb-5 rounded',
                children=[
                    # Your pie chart or other chart components go here
                ]
            ),
            
            
            
            
            
            html.Div(
                id='pie-chart',
                className='col text-center p-3 mb-5 rounded',
                children=[
                    dcc.Graph(
                        id='pie-chart-graph',
                        config={'staticPlot': False},
                        figure=px.pie(
                            data,
                            names='tweets_username',
                            title='Distribution of Tweets Among Users'
                        )
                    )
                ]
            )
        ]
    ),


html.Div(
    className='row py-3 mb-3 bg-warning shadow rounded',
    children=[
        html.Div(
            id='popularity-metrics',
            className='col text-center shadow-sm p-3 mb-5 bg-white rounded',
            # ... other properties
        )
    ]
),


    # # Tweet Insights Row 4
    # html.Div(className='row mb-3 py-3 col-12 bg-danger', children=[
    #     html.Div(id='tweet-insights', className='col-12')
    # ]),

    # Wordcloud row 5
    # html.Div(className='row mb-3', children=[
    #     html.Div([dcc.Graph(id='word-cloud')], className='col-12')
    # ]),


    # Main Content Row 6
    html.Div(className='row pt-3 col-sm-6 mb-3', children=[
        # For the engagement-metrics and time-analysis
        html.Div(className='row col-8 col-sm-12', children=[
            html.Div([dcc.Graph(
                id='engagement-metrics')],
                className='col-6 mb-3'),

            html.Div([dcc.Graph(id='time-analysis')], className='col-6 mb-3')
        ]),

        # For the top-contributors and most-liked-tweets
        html.Div(className='row col-4 py-3 mb-3', children=[
            html.Div([html.Table(id='top-contributors')],
                     className='col-4 bg-danger'),
            html.Div([html.Table(id='most-liked-tweets')], className='col-4')
        ])
    ]),


    # Footer Row 7
    html.Div([
        html.H1("Footer", style={
                'color': primary_colors['text'], 'textAlign': 'center'})
    ], className="py-3", style={'gridColumn': 'span 12'})
])


@app.callback(
    Output('total-tweets', 'children'),
    [Input('username-dropdown', 'value')]
)
def update_total_tweets(selected_username):
    if selected_username:
        total_tweets = data[data['tweets_username']
                            == selected_username].shape[0]
        return html.B(f"Total Tweets: {total_tweets}")
    else:
        return html.B("Total Tweets: N/A")


@app.callback(
    Output('engagement-metrics', 'figure'),
    Input('username-dropdown', 'value')
)
def update_graph(selected_username):
    filtered_df = data[data['tweets_username'] == selected_username]
    fig = px.bar(filtered_df, x='tweets_utc_date', y='tweets_likes_count')
    return fig



@app.callback(
    Output('popularity-metrics', 'children'),
    [Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')]
)
def update_popularity_metrics(start_date, end_date):
    if start_date and end_date:
        # Filter data for the selected date range
        filtered_df = data[(data['tweets_utc_date'] >= start_date) & 
                           (data['tweets_utc_date'] <= end_date)]
        
        # Aggregate data to get total likes and retweets per housemate
        agg_data = filtered_df.groupby('tweets_username').agg(
            total_likes=pd.NamedAgg(column='tweets_likes_count', aggfunc='sum'),
            total_retweets=pd.NamedAgg(column='tweets_retweet_count', aggfunc='sum')
        ).reset_index()
        
        # Create bar chart figure
        fig = px.bar(
            agg_data, 
            x='tweets_username', 
            y=['total_likes', 'total_retweets'],
            title='Popularity Metrics by Housemate'
        )
        
        return dcc.Graph(figure=fig)
    else:
        return 'Select a date range'





# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)
