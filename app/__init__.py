from flask import Flask
import os
import sendgrid
from sendgrid import SendGridAPIClient


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SENGRID_KEY=os.environ.get('SENDGRID_KEY'),
    )

    from . import portfolio

    app.register_blueprint(portfolio.bp)

    return app

    