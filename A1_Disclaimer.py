import dash_html_components as html
from utils import Header

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 6
            html.Div(
                [

                    html.Div(
                        [# Row 1
                            html.Div(
                                [
                                    html.H6("Disclaimer", className="subtitle padded"),
                                    html.Div(
                                        [
                                            html.P(
                                                "This app has been developed by Rongbin Ye beyond the model developed by Yun Yan,\
                                                as the deliverable for SmartSense by Digi for the MSBA/MBA Capstone project. \
                                                All rights are resevered by SmartSense by Digi and Capstone group 1. 2020. "
                                            )
                                        ],
                                        style={"color": "#7a7a7a"}
                                    ),
                                ],
                                className="row",
                            ),
                        # Row 2
                            html.Div(
                                [
                                    html.H6("Maintenance Notes", className="subtitle padded"),
                                    html.Div(
                                        [
                                            html.P("In the package, there are five major files and 3 key folders: assets, data and \
                                                                                               pages. These folders are the main component of the report, which is edible\
                                                                                               and upgradable for further usage."),
                                            html.Li(
                                                "Data Folder: This folder include the data for visualization and raw data\
                                                 The raw data has been stored in the name of data_final.csv. Meanwhile, the data\
                                                 for visualization has been stored in a manner of Page_purpose.csv, which refers\
                                                to page number_ dataname_figure."
                                            ),
                                            html.Li(
                                                "Asset Folder: This folder incldudes all the stylesheets and pictures been used.\
                                                If there is any accomodation or adjustment to the style or layout, the file \
                                                could be adjusted by editing new styles and logos in."
                                            ),
                                            html.Li(
                                                "Pages Folder: This key folder contains all the subpages been used\
                                                If there is any accomodation or adjustment to the style or layout, the file c\
                                                could be adjusted by editing new styles and logos in."),
                                            html.P(
                                                "The wrapper in this app is the app.py. "
                                            ),
                                            html.P(
                                                "The app.py will regenerate the full report with updated data,\
                                                 which enable one to predict the change timely. "
                                            ),
                                            html.P(
                                                "The model development and data cleansing process are recorded in the modeldevelopment.ipny,\
                                                and all the data used are based on the data process developed in the process."
                                            ),
                                        ],
                                        id="reviews-bullet-pts",
                                    ),
                                ],
                                className="row",
                            ),
                            # row 3
                            html.Div(
                                [
                                    html.H6("Further Potential", className="subtitle padded"),
                                    html.Div(
                                        [
                                            html.Div([
                                                html.Img(
                                                    src=app.get_asset_url("Data_Server.png"),
                                                    className="risk-reward",
                                                ),
                                                html.Br([]),
                                                html.A("Expansion of Functions", href='https://dash-gallery.plotly.host/Portal/', target="_blank"),
                                            ],className='four columns'),

                                            html.Div([
                                                html.Img(
                                                    src=app.get_asset_url("Cloud_Server.png"),
                                                    className="risk-reward",
                                                ),
                                                html.Br([]),
                                                html.A("Deployment On Cloud", href='https://dash.plotly.com/deployment', target="_blank"),
                                            ], className='four columns'),

                                            html.Div([
                                                html.Img(
                                                    src=app.get_asset_url("Function_.png"),
                                                    className="risk-reward",
                                                ),
                                                html.Br([]),
                                                html.A("Connection to Database", href='https://plotly.com/chart-studio-help/database-connectors/', target="_blank"),
                                            ], className='four columns'),
                                        ],
                                    ),
                                ],
                                className="row",
                            ),
                        ],
                        className="row ",
                    )
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )