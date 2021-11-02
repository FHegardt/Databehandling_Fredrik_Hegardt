import pandas as pd
from dash import dcc, html
import dash
from load_data1 import Stockdatalocal
from dash.dependencies import Output, Input
import plotly_express as px

stock_data_object = Stockdatalocal()

symbol_dict = dict(AAPL = "Apple", TSLA = "Tesla", NVIDIA = "Nividia")

stock_options_dropdown = [{"label": name, "value": symbol}
                         for symbol, name in symbol_dict.items()]
df_dict = {symbol: stock_data_object.stock_dataframe(symbol)
            for symbol in symbol_dict}
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Stocks viewer"),
    html.P("Choose a stock"),
    dcc.Dropdown(id='stock-picker-dropdown', className='',options = stock_options_dropdown,
    value = 'AAPL'
    ),
    dcc.Graph(id='stock-graph', classname = '')
 
    ])

@app.callback(
    Output("stock-graph","figure"),
    Input("stock-picker-dropdown", "value")
)
def update_graph(stock):

    dff_daily , dff_intraday = df_dict[stock]

    fig = px.line(dff_daily, x = dff.index, y = "close")

    return fig #fig object goes into output property i.e figure property


if __name__ == "__main__":
    app.run_server(debug=True)