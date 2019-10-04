# Python core imports
import os
import uuid

# Python third-party imports
import connexion
from flask import redirect, url_for


# Connexion setup
debugging = os.environ.get('debugging')
options = {"swagger_ui": debugging}

application = connexion.FlaskApp(
    __name__,
    specification_dir='config/',
    options=options
    )

application.add_api(
    'openAPI.yaml',
    base_path='/api',
    arguments={'title': 'Sample API'}
    )

# CSRF Key/Secret for forms
application.app.config.update(
    dict(
        SECRET_KEY=str(uuid.uuid4()),
        WTF_CSRF_SECRET_KEY=str(uuid.uuid4())
    )
)

# Max payload (to restrict large file uploads)
application.app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

# Re-direct to Swagger/OpenAPI UI
@application.app.route('/')
def index():
    return redirect(
        location=url_for(
            endpoint='/api./api_swagger_ui_index'
        ),
        code=302
    )


# Default robots reply
@application.app.route('/robots.txt', methods=['GET'])
def robots():
    return "User-agent: *\nDisallow: /"


# Run
if __name__ == '__main__':
    application.run()
