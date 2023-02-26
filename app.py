from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, current_user, logout_user
# from flask_sqlalchemy import SQLAlchemy
from routes import app


SECRET_KEY = '123123123'
app.config['SECRET_KEY'] = SECRET_KEY
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

import routes

if __name__ == '__main__':
    app.run(debug=True)

