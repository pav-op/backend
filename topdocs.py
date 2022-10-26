from flask import Blueprint, jsonify
from db_config import mysql

topdocs_blueprint = Blueprint('topdocs_blueprint', __name__)

@topdocs_blueprint.route('/topdocs', methods = ['GET'])
def topdocs():
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor()

        sql = "select name, genre, rating from doctors order by rating desc limit 10"

        cursor.execute(sql)
        row = cursor.fetchall()

        docs = {}
        count = 1

        for i in row:
            docs[count] = {
                    'name' : i[0],
                    'genre' : i[1],
                    'rating' : i[2]
                    }
            count += 1

        return jsonify(docs)


    except Exception as e:
        print(e)

    finally:
        if cursor and conn:
            cursor.close()
            conn.close()
