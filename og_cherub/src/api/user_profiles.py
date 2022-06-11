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
