import pymysql
from app import app
from db_config import mysql
from flask import jsonify, request, session

@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        return jsonify({'message' : 'We are already logged in', 'username': username})

    else:
        resp = jsonify({'message': 'Gay Bitch Go away (Unauthorized)'})
        resp.status_code = 401
        return resp

@app.route('/login', methods=['POST'])
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


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)

    return jsonify({'message': 'Logged Out Successfully'})

if __name__ == "__main__":
    app.run()
