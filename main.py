import datetime
import flask
from flask import Flask
from utils.db_connection import mysql
from flask import request
from flask import session

from blueprints.thread_services import thread_services
from blueprints.simple_login import simple_login
from blueprints.subs_services import subs_services
from blueprints.profile_services import profile_services
from blueprints.user_services import user_services
from blueprints.registration_services import registration_services
from blueprints.admin_services import admin_services


app = Flask(__name__, static_url_path="")

app.secret_key = "NEKI_RANDOM_STRING"

app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "toor"
app.config["MYSQL_DATABASE_DB"] = "mydb"
app.config["MYSQL_DATABASE_HOST"] = "localhost"

mysql.init_app(app)

app.register_blueprint(simple_login)
app.register_blueprint(registration_services)
app.register_blueprint(user_services)
app.register_blueprint(admin_services, url_prefix="/adminPanel")
app.register_blueprint(thread_services, url_prefix="/threads")
app.register_blueprint(subs_services, url_prefix="/subs")
app.register_blueprint(profile_services, url_prefix="/user")


@app.route("/")
@app.route("/index")
@app.route("/index.html")
def home():

    return app.send_static_file("index.html")

app.run("0.0.0.0", 80, threaded=True)