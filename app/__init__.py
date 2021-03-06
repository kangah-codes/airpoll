from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from config import config_by_name
from flask import Flask, render_template

# Define the WSGI application object
app = Flask(__name__)
db = SQLAlchemy(app)
flask_bcrypt = Bcrypt()
db.init_app(app)
flask_bcrypt.init_app(app)

# Configurations
app.config.from_object(config_by_name['dev'])
# Define the database object which is imported
# by modules and controllers


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return "NOT FOUND"

# Import a module / component using its blueprint handler variable (mod_auth)
from app.module.controllers import web as auth_module

# Register blueprint(s)
app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()