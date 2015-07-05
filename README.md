# Headlines Red Bullet Slack Add-on

This is a very simple add on for Slack. When a user runs a `/headlines [message]` command this script posts 2 messages to Slack. One to the room the user posted in and another to the designated headlines room. If they send it from the headlines room it will only be posted once.

## Stack

This project runs with Python (2.7) with dependencies installed via PIP and is set to run on Google App Engine.

Install dependencies with:
`pip install`

To run in dev and deploy you need to install (Google App Engine Launcher)[https://cloud.google.com/appengine/downloads]. From there you can hit `run` to run it locally or `deploy` to push it live (to your designated App Engine instance).

## Env variables

Env variables for this app are handled by creating a file called `secret_keys.py` in the root directory of this project. It should look like so:

SLACK_API_TOKEN = 'asfasd-asdfasd-adsfadf-adfadsfas'
HEADLINE_TOKEN = 'ASDASDASD'
HEADLINE_CHANNEL = 'headlines'
