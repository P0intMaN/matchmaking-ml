from flask import Flask

flask_app = Flask(__name__)
flask_app.config['SECRET_KEY'] = 'flask-secret-for-csrf-protection'

from project.src.app import routes
