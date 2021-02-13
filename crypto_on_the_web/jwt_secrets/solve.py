import jwt
import requests

# Challenge endpoint
URL = "http://web.cryptohack.org/jwt-secrets/"
SECRET_KEY = "secret"

def get_auth_route(token):
    return URL + f"authorise/{token}/"

# Generate token
token = jwt.encode({"username": "user", "admin": True}, SECRET_KEY, algorithm="HS256")
token = token.decode("utf-8")
print(token)

r = requests.get(get_auth_route(token))
print(r.content.decode("utf-8"))