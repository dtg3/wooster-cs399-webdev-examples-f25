from flask import Blueprint, jsonify, current_app

bp = Blueprint("main", __name__)

@bp.route("/hello")
def hello():
    return jsonify(message="Hello, Flask Factory!")
