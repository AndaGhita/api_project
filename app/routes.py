from flask import Flask
from __init__ import app #from the app module import app(__init__.py main)
from user.models import User

@app.route('/user/signup', methods=['GET'])
def signup():
    return User().signup()
