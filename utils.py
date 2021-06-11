import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("Smart-Sense.png"),
                        className="logo",
                    ),
                    html.Img(
                        src=app.get_asset_url("ND.png"),
                        className="logo",
                    ),
                    html.A(
                        html.Button("Contact", id="learn-more-button"),
                        href="mailto:rye@nd.edu?Subject=SmartSense%20Dashboard%20Problem>",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("SmartSense by Digi Call Center Digital Dashboard ")], # Name of the Board
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full Report",
                                href="/SmartSenseDash/final_Report", # Report need to be turned into Python
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Summary",
                href="/SmartSenseDash/Summary",
                className="tab first",
            ),
            dcc.Link(
                "Usage Data Monitor",
                href="/SmartSenseDash/Usage",
                className="tab",
            ),
            dcc.Link(
                "Call Data Monitor",
                href="/SmartSenseDash/Prediction",
                className="tab",
            ),
            dcc.Link(
                "Customer Satisfaction", href="/SmartSenseDash/Satisfaction", className="tab"
            ),
            dcc.Link(
                "Call Agent Monitor",
                href="/SmartSenseDash/Agents",
                className="tab",
            ),
            dcc.Link(
                "Disclaimer",
                href="/SmartSenseDash/Disclaimer",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table