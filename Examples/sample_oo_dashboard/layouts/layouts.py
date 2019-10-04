# Third-party imports
from dash_core_components import Location, Link as internal_link, Input
from dash_html_components import Link as external_link
from dash_html_components import Div, H1, P, Br
from dash_bootstrap_components import Container, Row, Col


class Layouts:
    '''
    Contains all default layouts for the application as callable functions.
    '''

    @staticmethod
    def base() -> Div:
        '''
        Returns a dash website base
        '''
        return Div([
            Location(id='url', refresh=False),
            external_link(
                rel='icon',
                href='assets/img/favicon.ico'
            ),
            Div(id='page_content')
        ])

    @staticmethod
    def index() -> Div:
        '''
        Returns the app index page
        '''
        return Container([
            Row([
                Col([
                    H1('Welcome to the Index Page'),
                    P(
                        'You can visit a second page by'
                        ' clicking the link below'
                    ),
                    internal_link('Hello Page', href='/hello'),
                ])
            ])
        ])

    @staticmethod
    def not_found() -> Div:
        '''
        Returns the 404 page not found page
        '''
        return Container([
            Row([
                Col([
                    H1('404 Page not found'),
                    internal_link('Home', href='/'),
                ])
            ])
        ])

    @staticmethod
    def hello() -> Div:
        '''
        Returns the hello page
        '''
        return Container([
            Row([
                Col([
                    H1('Hello, World!'),
                    Br(),
                    Input(
                        id='hello_input',
                        value='',
                        type='text',
                        placeholder='Enter name',
                        debounce=True
                    ),
                    Br(),
                    Div(id='hello_output'),
                    internal_link('Home', href='/'),
                ])
            ])
        ])
