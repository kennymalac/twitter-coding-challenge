from datetime import datetime
from time import mktime
import sys

import requests
from flask import Blueprint, make_response, session, jsonify

from .auth import get_twitter_token

import logging

logging.basicConfig(level=logging.DEBUG)

twitter_api = Blueprint('twitter', __name__)

@twitter_api.route('/timeline/<string:twitteruser_id>')
def fetch_user_timeline(twitteruser_id):
    '''Fetches an authorized user's timeline and serializes the output.'''

    print('Bearer ' + get_twitter_token())
    resp = requests.get(
        "https://api.twitter.com/1.1/statuses/user_timeline.json".rstrip(), params={
        'screen_name': twitteruser_id
    }, headers={
        'Authorization': 'Bearer {}'.format(get_twitter_token()),
    });

    try:
        tweets = resp.json()
    except JSONDecodeError as e:
        # 500 Internal Server Error
        return make_response(
            jsonify({'error': 'Parsing error'}), 500)

    timeline = []

    for tweet in tweets:
        timeline.append({
            'user': {
                'id': tweet['user']['id_str'],
                'screen_name': tweet['user']['screen_name'],
                'profile_image_url': tweet['user']['profile_image_url']
            },
            'tweet': {
                'id': tweet['id_str'],
                'text': tweet['text'],
                # UNIX time
                'posted': mktime(datetime.strptime(
                        tweet['created_at'], "%a %b %d %X %z %Y").timetuple())
            }
        })

    print(timeline)
    # Serialize the output into JSON
    try:
        return make_response(jsonify(timeline), 200)
    except JSONDecodeError as e:
        # 500 Internal Server Error
        return make_response(
            jsonify({'error': 'Parsing error'}), 500)
