from flask import Flask

app = Flask(__name__)

from twitter import routes