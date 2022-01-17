#!/usr/bin/python3
"""RestFul API actions for Users"""
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
import re
import os


email_patt = r'[\w\.]{2,30}\+?[\w]{0,10}@[\w\-]+\.[a-z]{2,5}\.?[a-z]{0,5}'
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
    except Exception as e:
        abort(400, description="Not a JSON")

    if 'full_name' not in data or data['full_name'] == '':
        abort(400, description="nombre completo faltante")
    if ',' in data['full_name']:
        abort(400, description="el nombre no puede contener comas")
    if 'email' not in data:
        abort(400, description="email faltante")
    if re.match(email_patt, data['email']) is None:
        abort(400, description="formato email errado")
    if 'city' not in data or data['city'] == '':
        abort(400, description="ciudad faltante")
    if ',' in data['city']:
        abort(400, description="la ciudad no puede contener comas")

    user = User(**data)
    try:
        user.save()
    except Exception as e:
        abort(400, description="email ya registrado")

    log_str = "[NEW USER],{},{},{},{},{}\n".format(
        str(user.created_at),
        str(user.id),
        user.full_name,
        user.email,
        user.city
        )

    log_path = "./log.txt"

    if not os.path.exists(log_path):
        header_str = "log_type,created_at,user_id,full_name,email,city\n"
        log_str = header_str + log_str

    with open(log_path, mode='a', encoding='utf-8') as a_file:
        a_file.write(log_str)

    return make_response(jsonify(user.to_dict()), 201)
