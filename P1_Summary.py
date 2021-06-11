import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder # Getting Data from source
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

# data loading
df_summary = pd.read_csv(DATA_PATH.joinpath("P1_Facts.csv"))
df_MainData = pd.read_csv(DATA_PATH.joinpath("MainData_DoW-Final.csv"))
prediction = pd.read_csv(DATA_PATH.joinpath("P3_Prediction_Output.csv"))

def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Overview of Project"),
                                    html.Br([]),
                                    html.P(
                                        "This dashboard is developed for Capstone Project between University of Notre Dame and \
                                         and SmartSense by Digi. The application has been designed to Predict the change of Call Volume, \
                                         , identify the key Drivers of Customer Satisfaction, and track the perfromance of Call Agents."
                                        ,
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product" # From Addin.css,
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div( # Left Top
                                [
                                    html.H6(
                                        ["Summary Of Tasks"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_summary)), # No such Function Avaliable
                                ],
                                className="six columns",
                            ),
                            html.Div( #Right Top
                                [
                                    html.H6(
                                        "Data Structure",
                                        className="subtitle padded",
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("Data_Structure_re.png"),
                                        className="risk-fancy",
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 6
                    html.Div(  # Prediction
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Prediction of Calls by year",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id='Prediction',
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=prediction['Y-W'],
                                                    y=prediction['Prediction'],
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
                                                title="Comparison of Volume",
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 4.5],
                                                    "showline": True,
                                                    "title": "Week of Projection",
                                                    "type": "category",
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [0, 2000],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "title": "Volume (Unit)",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    )
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
                    ),
                    # row 7
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )