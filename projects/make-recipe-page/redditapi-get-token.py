# Demonstrate how you can log in to the Reddit API to receive content that
# requires authentication, using only `requests` and your credentials.
# -----------------------------------------------------------------------------
# Following along from:
# https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c
# Not actually doing it because I don't have a Reddit account.
# I'm assuming that the purpose of this exercise is to understand APIs that
# require authentication & to practice learning new stuff outside of the course.

import requests
import os

client_id = os.environ["CLIENTID"]
client_secret = os.environ["SECRETTOKEN"]
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

username = os.environ["REDDITUSERNAME"]
password = os.environ["REDDITPASSWORD"]
login_data = {'grant_type': 'password',
              'username': username,
              'password': password}

headers = {'User-Agent': 'MyBot/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=login_data, headers=headers)

TOKEN = res.json()['access_token'] # Here's the required token.

headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)