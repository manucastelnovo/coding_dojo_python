from flask import render_template, request, url_for, redirect,Flask
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from datasource_service import deletePie, editPie, registerUser,getUser,registerPypie,getAllUserPie,getPieById
from wtforms.validators import InputRequired,Length, ValidationError
import sys
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

from models import User

app = Flask(__name__)
app.secret_key = 'super secret string'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'registerLogin'

@login_manager.user_loader
def load_user(user_id):
    return User.get(int(user_id))



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
    filling = StringField(validators=[InputRequired(),Length(min=3, max=45)])
    crust = StringField(validators=[InputRequired(),Length(min=3, max=20)])
    submit = SubmitField('Add Pie')

class EditPieForm(FlaskForm):
    name = StringField(validators=[InputRequired(),Length(min=3, max=20)])
    filling = StringField(validators=[InputRequired(),Length(min=3, max=20)])
    crust = StringField(validators=[InputRequired(),Length(min=3, max=20)])
    submit = SubmitField('Edit Pie')



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
        user = getUser(formRegister.email.data)
        new_user=User(user['firstname'],user['lastname'],user['email'],user['password'],user['id'])
        all_user_pie= getAllUserPie(new_user.id)
        login_user(new_user)
        name=current_user.firstname
        # user_id= current_user.id
        return redirect(url_for('dashboard'))
    
    if formLogin.validate_on_submit():
        user = getUser(formLogin.email.data)
        
        if user['email'] == formLogin.email.data and user['password'] == formLogin.password.data:
            
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
    formPie2=PypieForm()
    name=current_user.firstname
    user_id= current_user.id
    all_user_pie= getAllUserPie(user_id)
    
    
    if formPie2.validate_on_submit and request.method == 'POST':
        registerPypie(formPie2.name.data,formPie2.filling.data,formPie2.crust.data,user_id,0)
        print('pude registrar el pie')
        return redirect(url_for('dashboard'))
    return render_template('dashboard.html',form=formPie2,name=name,all_user_pie=all_user_pie)


@app.route('/pies', methods=['GET','POST']) 
@login_required
def pie():
    
    name=current_user.firstname
    user_id= current_user.id
    all_user_pie= getAllUserPie(user_id)
    url='https://localhost:5000/edit/'
    return render_template('pies.html',name=name,all_user_pie=all_user_pie,url=url)

@app.route('/edit/<int:pie_id>', methods=['GET','POST']) 
@login_required
def editPiePage(pie_id):
    formEditPie= EditPieForm()
    name=current_user.firstname
    if request == 'POST':
        editPie(pie_id,formEditPie.name.data,formEditPie.filling.data,formEditPie.crust.data)
    
    return render_template('edit_pie.html',form=formEditPie,name=name)


@app.route('/show/<int:pie_id>', methods=['GET','POST']) 
@login_required
def showPie(pie_id):
    formEditPie= EditPieForm()
    name=current_user.firstname
    current_pie = getPieById(pie_id)
    
    return render_template('show_pie.html',form=formEditPie,name=name,current_pie=current_pie)

@app.route('/delete/<int:pie_id>', methods=['GET','POST']) 
@login_required
def deletePiePage(pie_id):
    deletePie(pie_id)
    formPie=PypieForm()
    name=current_user.firstname
    user_id= current_user.id
    all_user_pie= getAllUserPie(user_id)
    
    return render_template('dashboard.html',form=formPie,name=name,all_user_pie=all_user_pie)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('registerLogin'))