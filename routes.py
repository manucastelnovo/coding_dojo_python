from flask import render_template, request, url_for, redirect,Flask
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from datasource_service import registerUser,getUser
from wtforms.validators import InputRequired,Length, ValidationError
import sys
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

from models import User

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'registerLogin'



class RegisterForm(FlaskForm):
    firstname = StringField()
    lastname = StringField(validators=[InputRequired(),Length(min=3, max=20)])
    email= EmailField(validators=[InputRequired(),Length(min=3, max=20)])
    password = PasswordField(validators=[InputRequired(),Length(min=8, max=20)])
    password2 = PasswordField(validators=[InputRequired(),Length(min=3, max=20)])
    submit = SubmitField('Register')
    
class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(),Length(min=3, max=20)])
    password = PasswordField(validators=[InputRequired(),Length(min=8, max=20)])
    submit = SubmitField('login')

class PypieForm(FlaskForm):
    name = StringField(validators=[InputRequired(),Length(min=3, max=20)])
    filling = StringField(validators=[InputRequired(),Length(min=3, max=20)])
    crust = StringField(validators=[InputRequired(),Length(min=3, max=20)])
    submit = SubmitField('Add Pie')







@login_manager.request_loader
def request_loader(email):
    user = getUser(email)
    return user



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/404', methods=['GET'])
def notfound():
    return render_template('404.html')

@app.route('/user', methods=['GET', 'POST'])
def registerLogin():
    formRegister = RegisterForm()
    
    formLogin= LoginForm()

    if formRegister.validate_on_submit():
        registerUser(formRegister.email.data,formRegister.firstname.data,formRegister.lastname.data,formRegister.password.data)
        print('se registro al usuario')
        return redirect(url_for('index'))
    
    if formLogin.validate_on_submit():
        user = getUser(formLogin.email.data)
        print('soy el user',user)
        if user['email'] == formLogin.email.data and user['password'] == formLogin.password.data:
            print("logueado")
            new_user=User(user['firstname'],user['lastname'],user['email'],user['password'],user['id'])
            login_user(new_user)
            return redirect(url_for('dashboard'))
        return redirect(url_for('registerLogin'))

    #     hashed_password = generate_password_hash(form.password.data, method='sha256')
        
    #     return redirect(url_for('login'))
    return render_template('register_login.html',formRegister=formRegister,formLogin=formLogin)


@app.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    form=PypieForm()
    return render_template('dashboard.html',form=form)
