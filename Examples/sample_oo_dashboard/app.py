# Python core imports
import os
import secrets

# Third-party imports
import dash
import dash_bootstrap_components as dbc
from flask import Flask

# Local imports (relative)
# from controllers.router import Router
# from controllers.hello import Hello
# from layouts.layouts import Layouts

# Local imports (absolute)
from Examples.sample_oo_dashboard.controllers.router import Router
from Examples.sample_oo_dashboard.controllers.hello import Hello
from Examples.sample_oo_dashboard.layouts.layouts import Layouts


# App variables
debug = os.getenv('DEBUG')

# Setting up flask for session management
application = Flask(__name__)
application.config.update(
    dict(
        SECRET_KEY=secrets.token_urlsafe(),
        WTF_CSRF_SECRET_KEY=secrets.token_urlsafe()
    )
)

# Setting up dash
app = dash.Dash(
    __name__,
    server=application,
    external_stylesheets=[dbc.themes.FLATLY],
    suppress_callback_exceptions=True
)

app.title = 'Sample webapp'
app.layout = Layouts.base()

# Registering the router
Router(app)

# Registering callbacks
Hello(app)

# Run
if __name__ == '__main__':
    app.run_server(debug=debug)