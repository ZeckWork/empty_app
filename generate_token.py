from jwt.api_jws import encode
import time

def generate_token(key_file_path, team_id, key_id):
    with open(key_file_path, "r") as key_file:
        private_key = key_file.read()

    payload = {
        "iss": team_id,
        "iat": int(time.time()),
        "exp": int(time.time()) + 20 * 60,
        "aud": "appstoreconnect-v1"
    }

    headers = {
        "kid": key_id
    }

    token = encode(payload, private_key, algorithm="ES256", headers=headers)
    return token


if __name__ == "__main__":
    import os

    key_file_path = "AuthKey.p8"
    team_id = os.environ["ISSUER_ID"]
    key_id = os.environ["KEY_ID"]

    token = generate_token(key_file_path, team_id, key_id)
    print(token)
