import pandas as pd
from dash import dcc, html
import dash

app = dash.Dash(__name__)

app.layout = html.Div([html.H1("Stocks viewer")])

if __name__ == "__main__":
    app.run_server(debug=True)