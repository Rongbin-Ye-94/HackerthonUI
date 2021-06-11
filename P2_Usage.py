import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib
import plotly.express as px

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

#Num Reading
A_reading = pd.read_csv(DATA_PATH.joinpath("P2_Num_Readings_All_scatter.csv"))
timestamp = A_reading['Y-W']
reading = A_reading['NUMREADINGS']

# Loading Data
weekdata = pd.read_csv(DATA_PATH.joinpath("P2_Week_Account.csv"))
weekdata['Y-W']=(weekdata['YEAROFREADINGS'].apply(lambda x: (str(x)[:4])))+'-'+(weekdata['WEEKOFREADINGS'].apply(lambda x: (str(x)[:2].zfill(2))))
P2_pie_platform = weekdata.groupby(['PLATFORM','Y-W']).agg({'NUMREADINGS':'sum'}).reset_index()
fig_platform_readings = px.pie(P2_pie_platform, values='NUMREADINGS', names='PLATFORM', title='Distribution of All Reading across platform')

P2_pie_account = weekdata.groupby(['ACCOUNTNAME']).agg({'NUMREADINGS':'mean'}).reset_index()
P2_pie_account = P2_pie_account.sort_values('NUMREADINGS', ascending = False).reset_index().iloc[:10,:]
fig_account_readings = px.pie(P2_pie_account, values='NUMREADINGS', names='ACCOUNTNAME', title='')

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

def create_layout(app):
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 2
            html.Div(
                [
                            # Row 1
                            html.Div(
                                [
                                    html.H6("Usage Data", className="subtitle padded"),
                                    html.Div(
                                        [
                                            html.P(
                                                "This tab inlcudes the finding\
                                                 related to the number of reading, which is the key representatives of the usage.\
                                                 The Call is a behavior largely depends on the \
                                                 the Usage and the deployment of the equipment.\
                                                 The number of reading specifically serves as a key indicator for usage. \
                                                "
                                            )
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                        ],
                        className="row",
                        ),
                    # Row 2 - Three Trends - NUMReading, NUMUNQUIE DEVCIES, NUMSITES
                            html.Div(
                                [ html.H6("Distribution of Reading across Top 10 Clients", className="subtitle padded"),
                                    html.Div(
                                    [
                                        dcc.Graph(
                                            id="pie-platform",
                                            figure=fig_platform_readings,
                                        ),
                                    ], className="six column"
                                    ),
                                    html.Div(
                                    [
                                         dcc.Graph(
                                                id="pie-platform",
                                                figure=fig_account_readings,
                                        ),
                                    ], className="six column"
                                    )
                        ],
                        className="row"
                        ),
                    # Row 3 - Breakdown by Platform/Premium
                            html.Div(
                                [
                            html.Div(
                                [
                                    html.H6("Historical Trends of Reading", className="subtitle padded"),
                                    dcc.Graph(
                                        id='Num_Reading',
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=timestamp,
                                                    y=reading,
                                                    marker={
                                                        "color": "#ff8b3d",
                                                        "line": {
                                                            "color": "rgb(255, 165, 0)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="Number of Reading",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=True,
                                                bargap=0.01,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0228945952895,
                                                    "y": -0.189563896463,
                                                    "orientation": "h",
                                                    "yanchor": "top",
                                                },
                                                margin={
                                                    "r": 100,
                                                    "t": 20,
                                                    "b": 10,
                                                    "l": 10,
                                                },
                                                showlegend=True,
                                                title="",
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 4.5],
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "category",
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [0, 2000],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    )
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )