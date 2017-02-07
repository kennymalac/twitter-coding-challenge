import base64

import requests
from flask import session
from flask_oauthlib.client import OAuth

# I am implementing basic application-level authentication without user-level features, such as POSTing a user tweet

# @twitter_api.route('/login')
# def login():
#     return twitter.authorize(
#         callback=url_for('twitter_api.oauth_authorized'))


oauth = OAuth()
twitter_auth = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    app_key='TWITTER'
)

# I couldn't figure out how to use Flask-Oauthlib for application-level auth with Twitter
# So I'm just doing it here myself manually
# We shouldn't have to launch the oauth2 token request as the token stays the same... oh well
def get_twitter_token():
    try:
        data = requests.post('https://api.twitter.com/oauth2/token', data={
            'grant_type': 'client_credentials'
        }, headers={
            'authorization': 'Basic ' + 
            base64.b64encode(('%s:%s' % (
                    twitter_auth.consumer_key,
                    twitter_auth.consumer_secret)).encode('utf-8')).decode('utf-8')
        }).json()
        print(data)
        # session['twitter_token'] = data['access_token']
        return data['access_token']
    except (requests.Timeout, requests.ConnectionError) as e:
        return None
