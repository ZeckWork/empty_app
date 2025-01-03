import time
import os
import jwt

def generate_token(key_file_path, team_id, key_id):
    with open(key_file_path, "rb") as key_file:
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

    try:
        token = jwt.encode(payload=payload, key=private_key, algorithm="ES256", headers=headers)
        return token
    except Exception as e:
        print(f'erro: {e}')


if __name__ == "__main__":
    key_file_path = "AuthKey_W3C39K74H2.p8"
    team_id = os.environ["ISSUER_ID"]
    key_id = os.environ["KEY_ID"]

    token = generate_token(key_file_path, team_id, key_id)
    print(token)
