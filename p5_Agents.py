import dash_html_components as html
from utils import Header
import pandas as pd
import pathlib
import plotly.express as px
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

# Loading Data
data = pd.read_csv(DATA_PATH.joinpath("P5_Maindata_HR.csv"))
data = data.reset_index()

most_experienced_5 = data.groupby('Assigned To').agg({'index':'count'}).sort_values('index', ascending = False).iloc[:5,:]
most_experienced_5 = most_experienced_5.reset_index()

low_efficiency_5 = data.groupby('Assigned To').agg({'Time To Close (hours)':'mean'}).sort_values('Time To Close (hours)', ascending = False).iloc[:5,:]
low_efficiency_5['Time To Close (hours)'] = round(low_efficiency_5['Time To Close (hours)'], 2)
low_efficiency_5 = low_efficiency_5.reset_index()
fig_lefficient = go.Figure(data=[go.Table(
    header=dict(values=['Name', 'Average TTCs']),
    cells=dict(values=[low_efficiency_5['Assigned To'], # 1st column
                       low_efficiency_5['Time To Close (hours)']], # 2nd column
                ))])

high_efficiency_5 = data.groupby('Assigned To').agg({'Time To Close (hours)':'mean'}).sort_values('Time To Close (hours)', ascending = True)
high_efficiency_5 = high_efficiency_5[high_efficiency_5['Time To Close (hours)']>0.1].iloc[:5,:]
high_efficiency_5['Time To Close (hours)'] = round(high_efficiency_5['Time To Close (hours)'],2)
high_efficiency_5 = high_efficiency_5.reset_index()
fig_hefficient = go.Figure(data=[go.Table(
    header=dict(values=['Name', 'Average TTCs']),
    cells=dict(values=[high_efficiency_5['Assigned To'], # 1st column
                       high_efficiency_5['Time To Close (hours)']], # 2nd column
                ))])

Average_TTCs = round(data['Time To Close (hours)'].mean(),2)
Average_item = round(data.groupby('Assigned To').agg({'index':'count'})['index'].mean(),2)

lastest_case = data.sort_values('Timestamp', ascending = False)
latest_Case = lastest_case.iloc[:1,:]["Assigned To"]

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page Appendix
            html.Div(
                [#sub-page
                            html.Div(
                                [
                                    html.H6("Call Agents Monitor", className="subtitle padded"),
                                    html.Div(
                                        [
                                            html.P(
                                                "This tab provides an user interface to monitor the performance of agents, \
                                                focusing on tracking the average perfcrmance of the team, the agents with \
                                                extrodinary progress, good performance and agents needs an in-depth conversation with. "
                                            ),
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="row",
                            ),
                            # Row 2
                            html.Div(
                                [html.H6(
                                    ["General Condition"],
                                    className="subtitle tiny-header padded",
                                ),
                                ],
                                className="row ",
                            ),
                            # Row 3
                            html.Div(
                                [html.Div(
                                    [html.H5(Average_TTCs,), html.P("Mean Time to Close (Hours)")],
                                    id="Mean TTC",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H5(Average_item), html.P("Mean Cases of Agent (Incidence)")],
                                    id="Mean Cases",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H5(latest_Case), html.P("Latest Case Assigned To       ")],
                                    id="Last Case",
                                    className="mini_container")
                                ],
                                className="row container-display ",
                            ),
                            #Row 4
                            html.Div(
                                [
                                    html.H6("Performance of Individuals", className="subtitle padded"),
                                    html.Div(
                                        [ html.P('''Five Fastest Responding Agents'''),
                                            html.Table(make_dash_table(high_efficiency_5))
                                        ],
                                        className = "six columns",
                                    ),
                                    html.Div(
                                        [ html.P('''Five Agents Need Some Help'''),
                                            html.Table(make_dash_table(low_efficiency_5))
                                        ],
                                        className="six columns",
                                    )
                                ],
                                className="row",
                            ),
                ],
                className="sub_page")
        ],
        className="page",
    )