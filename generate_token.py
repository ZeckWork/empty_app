from jwt import encode
import time
import os

def generate_token(key_file_path, team_id, key_id):
    # Abra o arquivo .p8 em modo binário ('rb') para garantir que a chave seja lida como bytes
    with open(key_file_path, "rb") as key_file:
        private_key = key_file.read()

    # Crie o payload
    payload = {
        "iss": team_id,
        "iat": int(time.time()),
        "exp": int(time.time()) + 20 * 60,  # Expira em 20 minutos
        "aud": "appstoreconnect-v1"
    }

    # Configure os cabeçalhos
    headers = {
        "kid": key_id
    }

    # Gere o token
    token = encode(payload, private_key, algorithm="ES256", headers=headers)
    return token


if __name__ == "__main__":
    key_file_path = "AuthKey.p8"
    team_id = os.environ["ISSUER_ID"]
    key_id = os.environ["KEY_ID"]

    token = generate_token(key_file_path, team_id, key_id)
    print(token)
