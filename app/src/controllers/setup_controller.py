from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from src import db
from src.models import AppStatus, User
from sqlalchemy.exc import OperationalError
from config import Config

setup_bp = Blueprint('setup', __name__)


def is_app_initialized():
    try:
        return AppStatus.get_status().is_initialized
    except OperationalError:
        return False


def set_app_initialized():
    status = AppStatus.get_status()
    status.is_initialized = True
    db.session.commit()


@setup_bp.route('/setup', methods=['GET', 'POST'])
def setup():
    if is_app_initialized():
        return redirect(url_for('home.home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Passwords do not match')
            return render_template('setup/setup.html')

        try:
            # Use the database URL from config
            current_app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI

            # Create all tables
            db.create_all()

            # Create admin user
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)

            set_app_initialized()

            db.session.commit()

            flash('Initial setup complete')
            return redirect(url_for('home.home'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error during setup: {str(e)}')
            return render_template('setup/setup.html')

    return render_template('setup/setup.html')