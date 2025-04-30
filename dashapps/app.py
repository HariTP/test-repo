import dash
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Simple Dash App"),
    dcc.Input(id='input-name', type='text', placeholder='Enter your name'),
    html.Br(),
    html.Div(id='output-greeting')
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
