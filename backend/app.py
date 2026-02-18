from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from config import Config
from models import db
from auth import auth_bp
from routes import api_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(api_bp, url_prefix="/api")

with app.app_context():
    db.create_all()

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")

@app.route("/leads-page")
def leads_page():
    return render_template("leads.html")

@app.route("/signup-page")
def signup_page():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run()
