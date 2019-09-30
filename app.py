import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

########### Define your variables ######

myheading1='Where Should You Eat?'
tabtitle = 'Restaurant Suggestions'
list_of_meals = ['Breakfast', 'Lunch', 'Dinner']
list_of_meal_images=['breakfast.jpeg', 'lunch.jpeg', 'dinner.jpg']
list_of_meal_options = ['Fast Casual', 'Sit Down', 'Surprise']
list_of_restaurants= {'Breakfast': {'Fast Casual': "Call Your Mother Deli", 'Sit Down': "Ted's Bulliten", 'Surprise':'Unconventional Diner'},
                      'Lunch': {'Fast Casual': "Sweetgreen", 'Sit Down': "Logan Tavern", 'Surprise':'Bluestone Lane'},
                      'Dinner': {'Fast Casual': "Chipotle", 'Sit Down': "Maydan", 'Surprise':'Taqueria Nacional'}},
list_of_images=['breakfast.jpg', 'lunch.jpg', 'dinner.jpg', 'fork.jpg]
sourceurl = 'https://www.yelp.com/'
githublink = 'https://github.com/mgeisreiter/dash-callbacks-radio'


########## Set up the chart

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    dcc.RadioItems(
        id='your_input_here',
        options=[
                {'label':list_of_meal_options[0], 'value':list_of_restaurants[0]},
                {'label':list_of_meal_options[1], 'value':list_of_restaurants[1]},
                {'label':list_of_meal_options[2], 'value':list_of_restaurants[2]},
                ],
        value=list_of_images[3],
        ),
    html.Div(id='your_output_here', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Book your Trip!', href=sourceurl),
    ]
)


########## Define Callback
@app.callback(Output('your_output_here', 'children'),
              [Input('your_input_here', 'value')])
def radio_results(image_you_chose):
    return html.Img(src=app.get_asset_url(image_you_chose), style={'width': 'auto', 'height': '50%'}),


############ Deploy
if __name__ == '__main__':
    app.run_server()
