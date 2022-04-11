from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.personality import Personality

personalities = Blueprint('personalities', 'personalities')

@personalities.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]
  personality = Personality(**data)
  db.session.add(personality)
  db.session.commit()
  return jsonify(personality.serialize()), 201

@personalities.route('/', methods=["GET"])
def index():
  personalities = Personality.query.all()
  return jsonify([personality.serialize() for personality in personalities]), 200

@personalities.route('/<id>', methods=["GET"])
def show(id):
  personality = Personality.query.filter_by(id=id).first()
  personality_data = personality.serialize()
  return jsonify(personality=personality_data), 200

@personalities.route('/<id>', methods=["PUT"]) 
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  personality = Personality.query.filter_by(id=id).first()

  if personality.profile_id != profile["id"]:
    return 'Forbidden', 403

  for key in data:
    setattr(personality, key, data[key])

  db.session.commit()
  return jsonify(personality.serialize()), 200

@personalities.route('/<id>', methods=["DELETE"]) 
@login_required
def delete(id):
  profile = read_token(request)
  personality = Personality.query.filter_by(id=id).first()

  if personality.profile_id != profile["id"]:
    return 'Forbidden', 403

  db.session.delete(personality)
  db.session.commit()
  return jsonify(message="Success"), 200