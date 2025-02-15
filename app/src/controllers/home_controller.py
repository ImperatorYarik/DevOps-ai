from flask import Blueprint, render_template, Response
from src.models import User
import time
import os

home_bp = Blueprint('home', __name__)



@home_bp.route('/')
def home():
    message = User.get_welcome_message()
    return render_template('home.html', message=message)


