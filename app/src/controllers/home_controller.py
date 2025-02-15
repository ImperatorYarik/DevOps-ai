from flask import Blueprint, render_template
from src.models import User

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    message = User.get_welcome_message()
    return render_template('home.html', message=message)

