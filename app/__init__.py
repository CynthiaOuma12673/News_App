from flask import Flask
from .config import config_options
from flask_bootstrap import Bootstrap

bootstrap =Bootstrap(app)

# initializing application
def create_application(config_name):
    app = Flask(__name__)



    # setting up configuration
    app.config.from_object(config_options[config_name])

    # initializing bootstrap
    bootstrap.init_app(app)

    # blueprint registration
    from .main import main_blueprint
    app.register_blueprint(main_blueprint)

    from .request import configure_request
    configure_request(app)

    return app


