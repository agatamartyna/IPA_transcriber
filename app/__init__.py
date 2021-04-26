from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = "kotwlodek"

from app import routes, models
