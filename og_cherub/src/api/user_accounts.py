from flask import Blueprint, jsonify, abort, request
from ..models import User, db
import sqlalchemy
from sqlalchemy import insert
from sqlalchemy import true, false

import hashlib
import secrets



def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('user_accounts', __name__, url_prefix='/user_accounts')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    users = User.query.all()  # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize())  # build list
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())


@bp.route('', methods=['POST'])
def create_account():

    if 'user_name' not in request.json or 'password' not in request.json:
        return abort(400)
    if len(request.json['password']) < 8 or len(request.json['user_name']) < 3:
        return abort(400)
    u = User(
        user_name=request.json['user_name'],
        password=scramble(request.json['password'])
    )
    db.session.add(u)  # prepare CREATE statement
    #db.session.commit()  # execute CREATE statement
    try:
        db.session.commit()
        return jsonify(u.serialize())
    except:
        return jsonify(False)


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    if 'user_name' not in request.json and 'password' not in request.json:
        return abort(400)

    u = User.query.get_or_404(id)

    if 'user_name' in request.json:
        if len(request.json['user_name']) < 3:
            return abort(400)
        u.user_name = request.json['user_name']
    if 'password' in request.json:
        if len(request.json['password']) < 8:
            return abort(400)
        u.password = scramble(request.json['password'])

    try:
        db.session.commit()
        return jsonify(u.serialize())
    except:
        return jsonify(False)
