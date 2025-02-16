from flask import Blueprint, render_template, Response, redirect, url_for
from src.models import User
from src.controllers.setup_controller import is_app_initialized
import time
import os

home_bp = Blueprint('home', __name__)



@home_bp.route('/')
def home():
    if not is_app_initialized():
        return redirect(url_for('setup.setup'))
    return render_template('home.html')


