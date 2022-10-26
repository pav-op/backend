from flask import Blueprint, jsonify, request
from db_config import mysql

signup_blueprint = Blueprint('signup_blueprint', __name__)

@signup_blueprint.route('/signup', methods = ['POST'])
def signup():
    conn = None
    cursor = None

    try:
        _json = request.get_json(silent=True)
        _username = _json['username']
        _password = _json['password']

        # logic is that if user does not exist, we create new users
        # An empty set from select from users would mean user does not exist
        if _username and _password:
            conn = mysql.connect()
            cursor = conn.cursor()

            sql = "SELECT * FROM users WHERE username=%s"
            sql_where = (_username, )

            cursor.execute(sql, sql_where)
            row = cursor.fetchone()

            if row:
                resp = jsonify({'message' : 'User Already Exists'})
                resp.status_code = 409
                return resp

            else:
                sql = "insert into users(username, password) values(%s, %s)"
                sql_where = (_username, _password, )

                cursor.execute(sql, sql_where)
                conn.commit()

                return jsonify({'message' : 'Signed up successfully'})

    except Exception as e:
        print("Error Happened")
        print(e)

    finally:
        if cursor and conn:
            cursor.close()
            conn.close()

