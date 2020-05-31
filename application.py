"""
    AN NGUYEN
    A simple Python Flask MVC webapp for DOGGO
    A user can be able to search, add to favorite list and delete a doggo from favorite list
"""
import flask
from flask.views import MethodView
from index import Index
from favorite import Favorite
from search import Search
from search import Result

application = flask.Flask(__name__)       # our Flask app

application.add_url_rule('/favorite/',
                view_func=Favorite.as_view('favorite'),
                methods=['GET'])

application.add_url_rule('/search/',
                view_func=Search.as_view('search'),
                methods=['GET', 'POST'])

application.add_url_rule('/result/',
                view_func=Result.as_view('result'),
                methods=['GET', 'POST'])

application.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000, debug=True)

