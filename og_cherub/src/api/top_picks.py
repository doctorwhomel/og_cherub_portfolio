from flask import Blueprint, jsonify, abort, request
from ..models import User, Profile, Pick, db
import sqlalchemy
from sqlalchemy import insert


bp = Blueprint('top_picks', __name__, url_prefix='/top_picks')


@bp.route('', methods=['POST'])
def populate_picks():

    active = request.json["id"]

    profiles = Profile.query.all()  # Compile profiles table
    top_picks = Pick.query.all()  # Compile top_picks table

    for p in profiles:  # identify active user
        if p.id == active:
            user = p

    for pk in top_picks:  # remove any pre-existing data for active user to avoid duplication of unique data type
        if pk.user_id == user.id:
            db.session.delete(pk)

    result = []

    for p in profiles:
        if p.user_location == user.user_location and p.age >= user.min_age and p.age <= user.max_age:  # Filter out incompatable profiles
            if p.gender == user.seeking or user.seeking == 'All':

                pk = Pick(  # construct Pick from compatiple profile
                    pick_id=p.id,
                    user_id=user.id
                )

                result.append(pk.serialize())
                db.session.add(pk)  # prepare CREATE statement

    db.session.commit()  # execute CREATE statement
    return jsonify(result)
