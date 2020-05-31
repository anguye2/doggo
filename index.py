from flask import render_template
from flask.views import MethodView
import gbmodel
import os

# INFO_API_KEY = os.environ['INFO_KEY']
# PHOTO_API_KEY = os.environ['PHOTO_KEY']

class Index(MethodView):
    def get(self):
        return render_template('index.html')
