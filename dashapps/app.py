import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from dataflow.dataflow import Dataflow

app = dash.Dash(__name__)

dataflow = Dataflow()
db = dataflow.connection("local_db")

# Get values
dummy = dataflow.variable("dummy")
dummy_1 = dataflow.variable("dummy_local")
dummy_2 = dataflow.variable("dummy_local_2")
dummy_3 = dataflow.secret("dummy_secret")
dummy_4 = dataflow.secret("dummy_secret_local")

app.layout = html.Div([
    html.H1("Simple Dash App"),
    dcc.Input(id='input-name', type='text', placeholder='Enter your name'),
    html.Br(),
    html.Div(id='output-greeting'),
    html.Hr(),
    html.H4("Debug Info"),
    html.Pre(f"DB connection: {db}"),
    html.Pre(f"dummy global variable: {dummy}"),
    html.Pre(f"dummy local variable: {dummy_1}"),
    html.Pre(f"dummy local variable 2: {dummy_2}"),
    html.Pre(f"dummy global secret: {dummy_3}"),
    html.Pre(f"dummy local secret: {dummy_4}")
])

@app.callback(
    Output('output-greeting', 'children'),
    [Input('input-name', 'value')]
)
def update_output(name):
    if name:
        return f"Hello, {name}!"
    return "Please enter your name."

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
