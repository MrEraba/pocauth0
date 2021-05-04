from flask import request
from jose import jwt


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header() -> str:
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                        "description":
                            "Authorization header is expected"}, 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must start with"
                            " Bearer"}, 401)
    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                        "description": "Token not found"}, 401)
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must be"
                            " Bearer token"}, 401)

    token = parts[1]
    return token


def verify_decorator_key(expected_token: str) -> None:
    decorator_auth = request.headers.get('DecoratorAuth', None)

    if not decorator_auth:
        raise AuthError({
            'description': 'DECORATOR KEY is expected'
        }, 403)

    if decorator_auth != expected_token:
        raise AuthError({
            'description': 'BAD KEY provided'
        }, 403)


def deserialize_token(token):
    deserialized_data = jwt.get_unverified_claims(token)
    return deserialized_data
