__author__ = 'Madison'

from flask import Flask

app = Flask(__name__, static_url_path='',
            # template_folder='app/templates'
            )
from app import views
