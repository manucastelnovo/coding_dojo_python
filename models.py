from flask_login import UserMixin

from datasource_service import getUserById


class User(UserMixin):
    
    def __init__(self, firstname,lastname,email,password,id):
        self.firstname = firstname
        self.lastname= lastname
        self.email=email
        self.password=password
        self.id=id

    @staticmethod
    def get(user_id):
        user_data=getUserById(user_id)
        
        user = User(id=user_data['id'], firstname=user_data['firstname'], lastname=user_data['lastname'], email=user_data['email'],password=user_data['password'])
        return user