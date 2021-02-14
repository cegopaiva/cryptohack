import jwt
import json
import requests

# Challenge endpoint
URL = "http://web.cryptohack.org/json-in-json/"
SECRET_KEY = "secret"

def create_session(username):
    return URL + f"create_session/{username}/"

def authorise(token):
    return URL + f"authorise/{token}/"

# Generate malicious token using JSON injection
params = "user%22%2C%20%22admin%22%3A%20%22True"
r = requests.get(create_session(params))

# Parse generated token
evil_token = json.loads(r.content.decode("utf-8"))["session"]

# Retrieve flag using token
r = requests.get(authorise(evil_token))
print(r.content.decode("utf-8"))