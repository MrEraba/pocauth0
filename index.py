import click
from dotenv import dotenv_values
from flask import Flask, jsonify
from flask.cli import AppGroup

from auth import AuthError
from client import get_token
from decorator_blueprint import decorator_bp

config = {**dotenv_values('.env')}

APP = Flask(__name__)
APP.register_blueprint(decorator_bp)

auth_cli = AppGroup('auth')


@auth_cli.command('login')
def login_auth0():
    response = get_token(config)
    print("*" * 20)
    print(response)


APP.cli.add_command(auth_cli)


@APP.errorhandler(AuthError)
def handle_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


@APP.route('/')
def health_check():
    return "Working", 200


if __name__ == '__main__':
    APP.run(port=config.get('FLASK_PORT', 3000))