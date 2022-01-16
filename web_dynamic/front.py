#!/usr/bin/python3
'''Starts a Flask Web Application'''
from flask import Flask, render_template
import uuid
from models import storage
from models.user import User
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''Coink is alive!'''
    return render_template('index.html',
                           cache_id=uuid.uuid4())

@app.route('/report', strict_slashes=False)
def report():
    '''shows all the users registrated'''
    users = storage.all(User).values()

    return render_template('report.html',
                           users=users,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    '''Main Function'''
    app.run(host='0.0.0.0', port=5000)
