import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    P1_Summary, # Page1_Summary,
    P2_Usage, # Page2_Usage
    P3_Prediction, # Page3_Prediction
    p4_Satisfaction,  # Page4_Satisfaction
    p5_Agents, # Page5_Strategy
    A1_Disclaimer # Append1_Disclaimer
)
# Import Pages From the Folders

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname): # For each page
    if pathname == "/SmartSenseDash/Summary":
        return P1_Summary.create_layout(app)
    elif pathname == "/SmartSenseDash/Usage":
        return P2_Usage.create_layout(app)
    elif pathname == "/SmartSenseDash/Prediction":
        return P3_Prediction.create_layout(app)
    elif pathname == "/SmartSenseDash/Satisfaction":
        return p4_Satisfaction.create_layout(app)
    elif pathname == "/SmartSenseDash/Agents":
        return p5_Agents.create_layout(app)
    elif pathname == "/SmartSenseDash/Disclaimer":
        return A1_Disclaimer.create_layout(app)
    elif pathname == "/SmartSenseDash/final_Report":
        return (
            P1_Summary.create_layout(app),
            P2_Usage.create_layout(app),
            P3_Prediction.create_layout(app),
            p4_Satisfaction.create_layout(app),
            p5_Agents.create_layout(app),
            A1_Disclaimer.create_layout(app)
        )
    else:
        return P1_Summary.create_layout(app)

if __name__ == "__main__":
    app.run_server(debug=True)