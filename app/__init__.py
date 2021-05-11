# app/__init__.py

from flask import Flask
from app.blueprints.friend  import friend_bp
from app.blueprints.home import home_bp

# Initialize the app
app = Flask(__name__,  instance_relative_config=True)

# register the blueprints
app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(friend_bp, url_prefix='/friend')

# Load the views
from app import routes

# Load the config file
app.config.from_object('config')
