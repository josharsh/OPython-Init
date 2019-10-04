# Third-party imports
from dash import Dash
from dash.dependencies import Input, Output


class Hello:
    '''
    Callback that greets the visitor
    '''

    def __init__(self, app: Dash):
        @app.callback(
            Output('hello_output', 'children'),
            [Input('hello_input', 'value')]
        )

        def update(hello_input: str):
            '''
            Takes in one arguement(s);
            - <hello_input>:   (str)

            Returns a layout_page matching requested pathname.
            '''
            # Some validation
            if len(hello_input) > 2:
                return f'Hello {hello_input}! Welcome to the app!'
