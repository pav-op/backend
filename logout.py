from logging import log

from flask import Blueprint, jsonify, session

logout_blueprint = Blueprint('logout_blueprint', __name__)

@logout_blueprint.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)

    return jsonify({'message': 'Logged Out Successfully'})
