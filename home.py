from flask import Blueprint, jsonify, request, session

home_blueprint = Blueprint('home_blueprint', __name__)

@home_blueprint.route('/')
def home():
    if 'username' in session:
        username = session['username']
        return jsonify({'message' : 'We are already logged in', 'username': username})

    else:
        resp = jsonify({'message': 'Gay Bitch Go away (Unauthorized)'})
        resp.status_code = 401
        return resp
