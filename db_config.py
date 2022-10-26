from flaskext.mysql import MySQL

from app import app

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = "varoo"
app.config['MYSQL_DATABASE_PASSWORD'] = "varoo"
app.config['MYSQL_DATABASE_DB'] = "backend"
app.config['MYSQL_DATABASE_HOST'] = "localhost"
mysql.init_app(app)
