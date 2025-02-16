from flask import Blueprint, render_template, Response, request, flash, redirect, url_for
from src.models import User

from src import db

settings_bp = Blueprint('settings', __name__)

@settings_bp.route("/settings")
def index():
    return render_template('settings/index.html')

def manage_users():
    pass

@settings_bp.route('/settings/register_user', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('settings/register_user.html')

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists', 'error')
            return render_template('settings/register_user.html')

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('User registered successfully', 'success')
        return redirect(url_for('settings.index'))

    return render_template('settings/register_user.html')
