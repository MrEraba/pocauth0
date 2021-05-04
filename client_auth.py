import http.client
import json


def get_token():
    conn = http.client.HTTPSConnection("artemis-testing.us.auth0.com")
    payload = {
        "client_id": "t3UYC1yGNavxsG8LuQoCcdNLz1t6rfWN",
        "client_secret": "tGcDE2A_ZsMhIx6t9-zBHTItWqtyZkpAdbIqgXnjPBhKCw1kuIqygmcxN-LEPBch",
        "audience": "https://artemis-testing.us.auth0.com/api/v2/",
        "grant_type": "client_credentials"
    }

    headers = {
        'content-type': "application/json"
    }

    conn.request("POST", "/oauth/token", body=json.dumps(payload), headers=headers)
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


if __name__ == "__main__":
    get_token()
