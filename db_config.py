from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = "varoo"
app.config['MYSQL_DATABASE_PASSWORD'] = "varoo"
app.config['MYSQL_DATABASE_DB'] = "backend"
app.config['MYSQL_DATABASE_HOST'] = "localhost"
mysql.init_app(app)
