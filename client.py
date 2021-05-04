import json
import requests

from config import config


def get_token(req_config):
    url = f"https://{req_config.get('AUTH0_DOMAIN')}/oauth/token"
    headers = {
        'content-type': "application/json"
    }
    payload = {
        "client_id": req_config.get('AUTH0_CLIENT_ID'),
        "client_secret": req_config.get('AUTH0_CLIENT_SECRET'),
        "audience": req_config.get('AUTH0_AUDIENCE'),
        "grant_type": req_config.get('AUTH0_GRANT_TYPE')
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return json.loads(r.text)


if __name__ == "__main__":

    data = get_token(config)
    print(type(data))
    print(data)
