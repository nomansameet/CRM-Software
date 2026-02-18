import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret123")
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwtsecret123")
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USERNAME = "nomansameet@gmail.com"
    MAIL_PASSWORD = "hello"
