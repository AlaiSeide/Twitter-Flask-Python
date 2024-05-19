from twitter import app, database
from twitter.models import User


with app.app_context():
    database.create_all()