import json
from requests_oauthlib import OAuth2Session


token_open = open('../secret/twitterapi.json', 'r')
token_load = json.load(token_open)

token_load['1']['app_key']

CK = token_load['1']['app_key']
CS = token_load['1']['app_secret']
AT = token_load['1']['oauth_token']
AS = token_load['1']['oauth_token_secret']
