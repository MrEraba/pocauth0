from flask import Flask, jsonify
from dotenv import dotenv_values

from auth import AuthError
from decorator_blueprint import decorator_bp

config = {**dotenv_values('.env')}
APP = Flask(__name__)
APP.register_blueprint(decorator_bp)


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