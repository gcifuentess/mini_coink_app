#!/usr/bin/python3
"""RestFul API actions for Users"""
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
import re


email_patt = r'[\w\.]{5,30}\+?[\w]{0,10}@[\w\-]+\.[a-z]{2,5}\.?[a-z]{0,5}'
email_patt = re.compile(email_patt)


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """
    Retrieves the list of all user objects
    or a specific user
    """
    all_users = storage.all(User).values()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    return jsonify(list_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Retrieves an user """
    user = storage.get(User, user_id)
    if not user:
        abort(404)

    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """
    Deletes a user Object
    """

    user = storage.get(User, user_id)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """
    Creates a user
    """
    try:
        data = request.get_json()
    except:
        abort(400, description="Not a JSON")

    if 'email' not in data:
        abort(400, description="email faltante")
    if 'full_name' not in data:
        abort(400, description="nombre completo faltante")
    if 'city' not in data:
        abort(400, description="ciudad faltante")

    if re.match(email_patt, data['email']) == None:
        abort(400, description="formato email errado")

    instance = User(**data)
    try:
        instance.save()
    except:
        abort(400, description="email ya registrado")

    return make_response(jsonify(instance.to_dict()), 201)
