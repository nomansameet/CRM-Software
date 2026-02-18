from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models import db, User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    user = User(
        username=data["username"],
        password=generate_password_hash(data["password"]),
        role=data.get("role", "sales")
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(message="User registered")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if user and check_password_hash(user.password, data["password"]):
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token)
    return jsonify(error="Invalid credentials"), 401
