from flask import Blueprint, jsonify, abort, request
from ..models import User, Profile, db
import sqlalchemy
from sqlalchemy import insert


bp = Blueprint('user_profiles', __name__, url_prefix='/user_profiles')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def all_profiles():
    profiles = Profile.query.all()  # ORM performs SELECT query
    result = []
    for p in profiles:
        result.append(p.serialize())  # build list
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def generate_picks(id: int):
    user = Profile.query.get_or_404(id)
    profiles = Profile.query.all()  # Compile profiles table
    result = []

    for p in profiles:
        if p.user_location == user.user_location and p.age >= user.min_age and p.age <= user.max_age:  # Filter out incompatable profiles
            if p.gender == user.seeking or user.seeking == 'All':
                result.append(p.serialize())
    return jsonify(result)

@bp.route('', methods=['POST'])
def create_profile():

    if 'seeking' not in request.json or 'min_age' not in request.json:
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