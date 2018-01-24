from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'INDEX'

@app.route('/welcome')
def sign_in():
    return 'SIGN IN'

@app.route('/who-are-you')
def sign_up():
    return 'SIGN UP'

@app.route('/<username>')
def user_profile(username):
    return 'User %s PAGE' % username

@app.route('/<username>/events')
def user_events(username):
    return 'USER %s EVENTS' % username
