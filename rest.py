
from app import app
from home import home_blueprint
from login import login_blueprint
from logout import logout_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(logout_blueprint)


if __name__ == "__main__":
    app.run()
