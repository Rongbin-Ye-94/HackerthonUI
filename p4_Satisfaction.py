#Page 4  CSAT
import dash_html_components as html
from utils import Header, make_dash_table
import pandas as pd
import pathlib
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pathlib
import plotly.express as px

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_csat_all = pd.read_csv(DATA_PATH.joinpath("P4_csat_data.csv"))
df_bar1 = df_csat_all.reset_index().groupby(['Score','Target Solution']).aggregate({'index':'count'})
df_bar1 = df_bar1.reset_index()
bar1 = px.bar(df_bar1, x='Score', y='index', color='Target Solution',
             labels={'index':'Number of Records'}, height=400)

df_bar2 = df_csat_all.groupby(['Score']).agg({'Time To Close (hours)':'mean'})['Time To Close (hours)']
df_bar2 = df_csat_all.reset_index()
bar2_X = df_bar2['Score']
bar2_y = df_bar2['Time To Close (hours)']
bar2 = px.bar(df_bar2, x='Score', y='Time To Close (hours)', color='Target Solution',
             labels={'Time To Close (hours)':'Mean Time to Close'}, height=400)

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 5
            html.Div(
                [
                    html.Div(
                        [# Row 1
                          html.H6(
                                        ["CSAT Data"], className="subtitle padded"
                                    ),
                                    html.P(
                                        [
                                            "This tab sheds lights on the customer satisfaction on the existing survey and\
                                            records. By extending the finding in the distribution of satisfied clients and\
                                            dissatisfied clients, a decision tree mode is used to find the relevant drivers."
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],className="row "
                            ),
                            #Row 2
                    html.Div([
                        html.H6(
                            ["General Distribution"], className="subtitle padded"
                        ),
                    ], className='row'),
                            html.Div(
                                [
                                    html.Div([
                                    dcc.Graph(
                                        id='General-bar-volume',
                                        figure = bar1
                                    )
                                    ], className="six columns"),

                                    html.Div([
                                    dcc.Graph(
                                        id='General-bar-volume',
                                        figure=bar2
                                    )
                                ], className="six columns")
                        ],
                        className="row ",
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Decision Tree Model"],
                                        className="subtitle tiny-header padded",
                                    ),
                                ],
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    #row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div([
                                        html.P(['''Per Findings, a decision tree model has been developed here \
                                        to uncover the importance of different factors influcing the customer satisfaction\
                                        substantially. ''']),
                                        html.P(['''Limited to data collected, the tree model's dependent variable 
                                        is defined as "Satisfied" or "Not Satisfied", instead of locating at a specific score.
                                        The satisfied is defined as the clients rate services at 4 to 5, and the dissatisfied
                                        is defined as clients rated service lower than 4.'''
                                        ])
                                    ])
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # row 4
                    html.Div(
                        [
                            html.Div(
                                [ html.P('''The tree model is as followed:'''),
                                    html.Img(
                                        src=app.get_asset_url("P4_Tree.png"),
                                        className="risk-fancy ",
                                    )],
                            ),
                        ],
                        className="row",
                    ),
                    # row 5
                    html.Div([
                        html.Div(
                            [html.Br([]),
                             html.H6('''Takeaway & Explanation'''),
                             html.Li('Time to Close plays a crucial impact on clients satisfaction.'),
                             html.Li('Log in related, connectivity, alert to clients are key issues to win the clients.'),
                             html.Li('One specific Agent has specific impacts on the satisfaction.')
                             ],
                            className="six columns",
                        )],
                        className = "row"
                    )
                ], className="sub_page"
            ),
        ],
        className="page",
    )