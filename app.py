from flask import Flask
from flask_scss import Scss
from flask_session import Session

app = Flask(__name__)
app.config.from_object('settings')
Scss(app, static_dir='static', asset_dir='assets')
Session(app)
