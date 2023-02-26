from flask import render_template, request, url_for, redirect,Flask
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from datasource_service import registerUser


app = Flask(__name__)


class RegisterForm(FlaskForm):
    firstname = StringField()
    lastname = StringField()
    email= EmailField()
    password = PasswordField()
    password2 = PasswordField()
    submit = SubmitField('Register')
    
class LoginForm(FlaskForm):
    username = StringField()
    email = StringField('email')
    password = PasswordField('password')
    submit = SubmitField('login')

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
        registerUser('1111@gmail.com','2','3','4')
        print('se registro al usuario')

    #     hashed_password = generate_password_hash(form.password.data, method='sha256')
        
    #     return redirect(url_for('login'))
    return render_template('register_login.html',formRegister=formRegister,formLogin=formLogin)



