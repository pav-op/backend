from flask import Blueprint, jsonify, request, session

from db_config import mysql

login_blueprint = Blueprint('login_blueprint', __name__)

@login_blueprint.route('/login', methods = ['POST'])
def login():
    conn = None
    cursor = None

    try:
        _json = request.get_json(silent=True)
        _username = _json['username']
        _password = _json['password']

        if _username and _password:
            conn = mysql.connect()
            cursor = conn.cursor()

            sql = "SELECT * FROM users WHERE username=%s"
            sql_where = (_username,)

            cursor.execute(sql, sql_where)
            row = cursor.fetchone()

            if row:

                if row[2] == _password:
                    session['username'] = row[1]
                    return jsonify({'message': 'Logged in successfully'})

                else:
                    resp = jsonify({'message': 'Bad Request: Invalid Password'})
                    resp.status_code = 401
                    return resp

            else:
                resp = jsonify({'message': 'Bad Request: Invalid Creds'})
                resp.status_code = 400
                return resp


    except Exception as e:
        print("Error Happened")
        print(e)

    finally:
        if cursor and conn:
            cursor.close()
            conn.close()
