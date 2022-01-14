#!/usr/bin/python3
'''Starts a Flask Web Application'''
from flask import Flask, render_template
import uuid
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''Coink is alive!'''

    return render_template('index.html',
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    '''Main Function'''
    app.run(host='0.0.0.0', port=5000)
