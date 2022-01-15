#!/usr/bin/python3
"""Flask Application API"""
from models import storage
from api.v1.views import app_views
from flask import Flask, render_template, make_response, jsonify

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_db(error):
    """Close Storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """Main Function"""
    app.run(host='0.0.0.0', port=5001, threaded=True)
