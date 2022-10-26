from datetime import timedelta

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

app.secret_key = "nigga"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

from home import home_blueprint
from login import login_blueprint
from logout import logout_blueprint
from signup import signup_blueprint
from topdocs import topdocs_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(logout_blueprint)
app.register_blueprint(signup_blueprint)
app.register_blueprint(topdocs_blueprint)

