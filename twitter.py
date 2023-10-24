from dash import html
from dash import dcc
import dash
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px


external_stylesheets = [
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']


# Load the data into a DataFrame
file_path = 'Updated_Combined_BBNaijaAllStars_2023_Data.xlsx'  # Update this path
df = pd.read_excel(file_path)

# Inspect the first few rows of the DataFrame
# print(df.head(2))
# print(df.head(5))
print(df.columns)
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

unique_usernames = df['Username'].unique()
username_options = [{'label': username, 'value': username}
                    for username in unique_usernames]

time_range_options = [
    {'label': 'Last 7 Days', 'value': '7d'},
    {'label': 'Last 30 Days', 'value': '30d'},
    {'label': 'Last 3 Months', 'value': '3m'},
    # Add more as needed
]


# Define the app layout
app.layout = html.Div(className='container-fluid alert alert-primary', style={'backgroundColor': primary_colors['background'], 'textAlign': 'center'}, children=[

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
            className='col-12 col-md-3 my-1',
            style={'marginLeft': 'auto', 'marginRight': 'auto'}
        ),
        html.Div(dcc.Dropdown(
            id='time-dropdown',
            options=time_range_options,
            style={'minWidth': '200px', 'maxWidth': '250px'}
        ),
            className='col-sm-3 my-1'
        ),

        html.Div(dcc.Dropdown(
            id='hashtag-dropdown',
            options=time_range_options,
            style={'minWidth': '200px', 'maxWidth': '250px'}
        ),
            className='col-sm-3 my-1'
        ),

        html.Div(dcc.Dropdown(
            id='sentiment-dropdown',
            options=time_range_options,
            style={'minWidth': '200px', 'maxWidth': '250px'}
        ),
            className='col-sm-3 my-1'
        ),
    ]),



    # Overview Metrics Row 3
    html.Div(className='row py-3 mb-3 bg-warning', children=[
        html.Div(id='total-tweets', className='col-3 text-center'),
        html.Div(id='unique-contributors', className='col-3'),
        html.Div(id='avg-likes', className='col-3'),
        html.Div(id='avg-retweets', className='col-3')
    ]),


    # # Tweet Insights Row 4
    # html.Div(className='row mb-3 py-3 col-12 bg-danger', children=[
    #     html.Div(id='tweet-insights', className='col-12')
    # ]),


    # Wordcloud row 5
    html.Div(className='row mb-3', children=[
        html.Div([dcc.Graph(id='word-cloud')], className='col-12')
    ]),


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
        total_tweets = df[df['Username'] == selected_username].shape[0]
        return f"Total Tweets: {total_tweets}"
    else:
        return "Total Tweets: N/A"
    
    
@app.callback(
    Output('engagement-metrics', 'figure'),
    Input('username-dropdown', 'value')
)
def update_graph(selected_username):
    filtered_df = df[df['Username'] == selected_username]
    fig = px.bar(filtered_df, x='UTC Date', y='Likes count')
    return fig



# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)
