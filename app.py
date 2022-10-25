from datetime import timedelta
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

app.secret_key = "nigga"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
CORS(app)
