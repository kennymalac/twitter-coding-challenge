from app import app
#import auth
from twitter.api import twitter_api

app.register_blueprint(twitter_api, url_prefix='/api/twitter')
