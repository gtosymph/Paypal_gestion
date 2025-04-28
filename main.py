import os
import sys
import requests
from requests.auth import HTTPBasicAuth

def get_access_token():
    client_id = os.getenv('PAYPAL_CLIENT_ID')
    client_secret = os.getenv('PAYPAL_CLIENT_SECRET')
    if not client_id or not client_secret:
        print("❌ Veuillez définir les variables d'environnement PAYPAL_CLIENT_ID et PAYPAL_CLIENT_SECRET.")
        sys.exit(1)

    url = 'https://api.sandbox.paypal.com/v1/oauth2/token'
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en_US',
    }
    data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post(url,
                             auth=HTTPBasicAuth(client_id, client_secret),
                             headers=headers,
                             data=data)
    if response.status_code == 200:
        token = response.json().get('access_token')
        print("✅ Connexion réussie !")
        print(f"Token d’accès : {token}")
    else:
        print(f"❌ Échec de la connexion (HTTP {response.status_code})")
        print("Détails :", response.text)
        sys.exit(1)

if __name__ == '__main__':
    get_access_token()
