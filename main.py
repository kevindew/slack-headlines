"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
from flask import request
from slacker import Slacker
import json
import datetime

app = Flask(__name__)
slack = Slacker('xoxp-2175777328-2178938430-6767734195-dc1344')

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/headline', methods=['POST'])
def hello():
    """Send a headline."""
    # if request.form['token'] != 'zSf7gubrdsb798Lrdi18AkfS':
        # return 'Bad Request', 400
    icon_url = 'https://pbs.twimg.com/profile_images/1484608334/mcdonaldtre_400x400.jpg'
    username = 'Trevor McDonald'
    user = slack.users.info(request.form['user_id'])
    attachments = [{
        'author_name': '@' + request.form['user_name'],
        'author_icon': user.body['user']['profile']['image_24'],
        'text': request.form['text'],
        'fields': [{
            'title': 'Discuss in',
            'value': '#' + request.form['channel_name'],
            'short': True
        }]
    }]
    slack.chat.post_message('#playtime', '', username=username, icon_url=icon_url, attachments=json.dumps(attachments), parse='full')

    return '', 204

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
