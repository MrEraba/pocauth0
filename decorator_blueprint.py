from flask import Blueprint, jsonify

from config import config
from auth import (
    get_token_auth_header, deserialize_token, verify_decorator_key,
)
from login_observer import company_subject_factory


decorator_bp = Blueprint('decorator', __name__, url_prefix='/decorate')


@decorator_bp.route('/', methods=['POST'])
def decorate_token():

    verify_decorator_key(config['AUTH0_TOKEN_DECORATOR_KEY'])
    login_subject = company_subject_factory('Artemis Health', 'Zeus Data')
    response = login_subject.notify().companies

    return jsonify(response), 200


@decorator_bp.route('/test_hook')
def test_auth0_hook():
    res_data = dict()
    token = get_token_auth_header()
    deserialized_data = deserialize_token(token)
    res_data['from_hook'] = deserialized_data
    return jsonify(res_data), 200