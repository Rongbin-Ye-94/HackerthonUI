import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib
import plotly.express as px
import plotly.graph_objects as go


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

# Loading Data
data = pd.read_csv(DATA_PATH.joinpath("P3_Platform.csv"))

# Freshtemp
data1 = data[data['Target Solution'] == 'freshtemp']
year_list = data1['Y-W']
TTc_list = data1['TTCs']
volume_list = data1['counts of calls']
fig_freshtemp = px.bar(data1, x = 'Y-W', y = 'TTCs',title='Time to Close Freshtemp',range_y=[0,1000])
fig_freshtemp_Call = px.scatter(data1, x = 'Y-W', y = 'counts of calls',title='Count of Calls of Freshtemp',range_y=[0,1000])

# safetemp
data2 = data[data['Target Solution'] == 'safetemps']
year_list_1 = data2['Y-W']
TTc_list_1 = data2['TTCs']
volume_list_1 = data2['counts of calls']
# smarttemps
data3 = data[data['Target Solution'] == 'smarttemps']
year_list_2 = data3['Y-W']
TTc_list_2 = data3['TTCs']
volume_list_2 = data3['counts of calls']

# tempalert
data4 = data[data['Target Solution'] == 'tempalert']
year_list_3 = data4['Y-W']
TTc_list_3 = data4['TTCs']
volume_list_3 = data4['counts of calls']

# Pie Chart 1
df = pd.read_csv(DATA_PATH.joinpath("P3_pie_platform.csv"))
fig = px.pie(df, values='index', names='Target Solution', title='Distribution of calls across platform',
             labels={'index':'Incidence of Call'})
fig.update_layout(legend_orientation="h")
fig.update_layout(legend=dict(x=-0.75, y=1.2))
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_traces(hole=.2, hoverinfo="label+percent+name")

# Pie Chart 2
df_premium = pd.read_csv(DATA_PATH.joinpath("P3_premium_piechart.csv"))
fig_premium = px.pie(df_premium, values='index', names='Premium', title='Distribution of calls across Premium',
                     labels={'index':'Incidence of Call'})
fig_premium.update_layout(legend=dict(x=-0.75, y=1.2))
fig_premium.update_traces(hole=.2, hoverinfo="label+percent+name")

#Pie Chart 3
df_installation = pd.read_csv(DATA_PATH.joinpath("P3_pie_installation.csv"))
fig_installation = px.pie(df_installation, values='index', names='Installation Type', title='Distribution across Installation',
                          labels={'index':'Incidence of Call'})
fig_installation.update_layout(legend_orientation="h")
fig_installation.update_layout(legend=dict(x=-0.75, y=1.2))
fig_installation.update_traces(hole=.2, hoverinfo="label+percent+name")

# Table 1
prediction = pd.read_csv(DATA_PATH.joinpath("P3_Prediction_Output.csv"))
fig_predict = go.Figure(data=[go.Table(
    header=dict(values=['Y-W', 'Prediction']),
    cells=dict(values=[prediction['Y-W'], # 1st column
                       prediction['Prediction']], # 2nd column
                ))])

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 5
            html.Div(
                [
                    # Row 1 - Introduction
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Call Data"], className="subtitle padded"
                                    ),
                                    html.P(
                                        [
                                            "This tab provides the finding and predictive model of the calling data and\
                                            records. After exploring the distribution across platforms, installation and\
                                            premium member, the group decided to use ARIMAX model to predict the volume."
                                        ],
                                        style={"color": "#7a7a7a"},
                                    )
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Br([]),
                                    html.H6(
                                        ["Volume Trace by Platform"],
                                        className="subtitle tiny-header padded",
                                    ),
                                    html.Div(
                                        [
                                            dcc.Graph(
                                                id='TCC',
                                                figure={
                                                    "data": [
                                                        go.Scatter(
                                                            x=year_list,
                                                            y=volume_list,
                                                            marker={
                                                                "color": "#3089EF",
                                                                "line": {
                                                                    "color": "rgb(48, 137, 239)",
                                                                    "width": 2,
                                                                },
                                                            },
                                                            name="Fresh Temp",
                                                        ),
                                                        go.Scatter(
                                                            x=year_list,
                                                            y=volume_list_1,
                                                            marker={
                                                                "color": "#90EE90",
                                                                "line": {
                                                                    "color": "rgb(144, 238, 144)",
                                                                    "width": 2,
                                                                },
                                                            },
                                                            name="Safe Temps",
                                                        ),
                                                        go.Scatter(
                                                            x=year_list,
                                                            y=volume_list_2,
                                                            marker={
                                                                "color": "#FF9933",
                                                                "line": {
                                                                    "color": "rgb(255, 153, 51)",
                                                                    "width": 2,
                                                                },
                                                            },
                                                            name="Smart Temps",
                                                        ),
                                                        go.Scatter(x = year_list_3,
                                                               y = volume_list_3,
                                                               marker={
                                                                "color": "#000099",
                                                                "line": {
                                                                    "color": "rgb(0, 0, 153)",
                                                                    "width": 2,
                                                                },
                                                            },
                                                            name="Temp Alert"
                                                        )
                                                    ],
                                                    "layout": go.Layout(
                                                        autosize=True,
                                                        bargap=0.01,
                                                        font={"family": "Raleway", "size": 10},
                                                        height=200,
                                                        hovermode="closest",
                                                        legend={
                                                            "x": -0.05,
                                                            "y": -0.5,
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
                                                        title="Historical Call Volumes",
                                                        xaxis={
                                                            "autorange": True,
                                                            "range": [-0.5, 4.5],
                                                            "showline": True,
                                                            "title": "Week of Year",
                                                            "type": "category",
                                                        },
                                                        yaxis={
                                                            "autorange": True,
                                                            "range": [0, 2000],
                                                            "showgrid": True,
                                                            "showline": True,
                                                            "title": "Volume of Calls",
                                                            "type": "linear",
                                                            "zeroline": False,
                                                        },
                                                    ),
                                                },
                                                config={"displayModeBar": False},
                                            )
                                        ],
                                    )
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 3
                    html.Div(
                        [   html.H6(
                                        ["Explore the Distribution"],
                                        className="subtitle tiny-header padded",
                                    ),
                        ],
                        className="row ",
                    ),
                    #Additional row
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    dcc.Graph(
                                        id="Pie-tester",
                                        figure=fig,
                                    )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    dcc.Graph(
                                        id="Pie-Premium",
                                        figure=fig_premium
                                    )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    dcc.Graph(
                                        id="Pie-installation",
                                        figure=fig_installation,
                                    )
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                    #row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    dcc.Graph(
                                        id="Pie-installation",
                                        figure=fig_installation,
                                    )
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                    #Row 6
                    html.Div(
                        [html.H6(
                            ["ARIMAX Model"],
                            className="subtitle tiny-header padded",
                        ),
                        html.P('''Based on the findings, a Auto Regression Intergrated Moving Average with Explanatory Variable \
                        (ARIMAX) model(3,0,2) has been developed to predict the volume in next few weeks. '''),
                        ],
                        className="row ",
                    ),
                    #Row 7
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Img(
                                        src=app.get_asset_url("Model_Summary.png"),
                                        className="risk-fancy",
                                    ),
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
                    ),
                    #Row 8
                    html.Div(
                        [html.H6(
                            ["General Performance of Model"],
                            className="subtitle tiny-header padded",
                        ),
                        html.P('The model has a moderate performance in predicting the absolute volume, \
                        but it provides an accurate insight into the growth and decrease of the call volumes\
                        in the future. With data of better resolution and more quantitative features, the model\
                        could provide a more accurate estimation on the volume.'
                        ),
                        ],
                        className="row ",
                    ),
                    #Row 9
                    html.Div(
                        [
                            html.Img(
                                src=app.get_asset_url("Prediction.png"),
                                className="risk-fancy",
                            ),
                        ],
                        className="row"
                    )
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )