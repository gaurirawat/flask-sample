from flask import Blueprint
home_bp = Blueprint('home', __name__)

@home_bp.route('/enter/')
def enter():
    return "Enter into home"

@home_bp.route('/leave/')
def leave():
    return "Leave home"