# Import all the module
import dash
from dash import dcc, html
from flask import Flask
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Initialize the app
server = Flask(__name__)
app = dash.Dash(__name__,server=server, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

# Read the dataset
df = pd.read_csv('count.csv')
df1 = pd.read_csv('data.csv')


# Build the components
header_components = html.H1('Traffic Analysis Dashboard',style={'color':'darkcyan','align':'center'})

# visual components
#component 1
countfig = go.FigureWidget()
countfig.add_scatter(name='bus',x=df['Time'],y=df['bus'],fill='tonexty')
countfig.add_scatter(name='car',x=df['Time'],y=df['car'],fill='tonexty')
countfig.update_layout(title = "Vehicle Time Line")

# Components 2
countfig_cum = go.FigureWidget()
countfig_cum.add_scatter(name='bus',x=df['Time'],y=df['bus'].cumsum(),fill='tonexty')
countfig_cum.add_scatter(name='car',x=df['Time'],y=df['car'].cumsum(),fill='tonexty')
countfig_cum.update_layout(title = "Cumulative traffic")

# Components 3
indicator = go.FigureWidget(
    go.Indicator(
        mode="gauge+number",
        value = df['car'].mean(),
        title={'text':'Speed km/h'}
    )
)
indicator.update_layout(title="Average Car speed")

# components 4
indicator1 = go.FigureWidget(
    go.Indicator(
        mode="gauge+number",
        value = df['bus'].mean(),
        title={'text':'Speed km/h'}
    )
)
indicator1.update_layout(title="Average Bus speed")

# components 5
piefig = go.FigureWidget(
    px.pie(
        labels=['car','bus'],
        values = [df['car'].sum(),df['bus'].sum()]
    )
)
piefig.update_layout(title='Traffic Distribution')



# Design the app layout
app.layout = html.Div(
    [
        dbc.Row([
            header_components
        ]),
        dbc.Row(
            [dbc.Col(
                [dcc.Graph(figure=countfig)]
            ),dbc.Col(
                [dcc.Graph(figure=countfig_cum)]
            )]
        ),
        dbc.Row(
            [dbc.Col(
                [dcc.Graph(figure=indicator)]
            ),dbc.Col(
                [dcc.Graph(figure=indicator1)]
            ),dbc.Col(
                [dcc.Graph(figure=piefig)]
            )]
        ),
    ]
)



# Run the app
app.run_server(debug = True)
























