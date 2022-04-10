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