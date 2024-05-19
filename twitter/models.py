from twitter import database

class User(database.Model):
    __tablename__ = 'usuarios'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), unique=True)
    email = database.Column(database.String(120), unique=True)