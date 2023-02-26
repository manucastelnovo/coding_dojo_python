from flask_login import UserMixin


class User(UserMixin):
    
    def __init__(self, firstname,lastname,email,password,id):
        self.firstname = firstname
        self.lastname= lastname
        self.email=email
        self.password=password
        self.id=id