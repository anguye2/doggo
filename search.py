from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
import api
import urllib,json
from flask import request, render_template


class Search(MethodView):

    def get(self):
        breeds = api.get_breed()   
        return render_template('search.html', breeds=breeds)

class Result(MethodView):

    def get(self):                                             
        breed_name = request.args.get('selected_breed')                             
        breeds, info, photo = api.info(breed_name)

        return render_template('result.html', selected_breed=breed_name, breeds=breeds, image=photo, selected_info=info)

    def post(self):
        """
        Accepts POST requests and gets the data from the form
        Redirect to search when completed.
        """
        model = gbmodel.get_model()
        breed_name = request.form.get('selected_breed') 
        breed_image = request.form.get('selected_image') 
        breeds, info, photo = api.info(breed_name)
        db_info = api.db_info(info, photo)
        model.insert(db_info)
        return render_template('result.html', selected_breed=breed_name, breeds=breeds, image=breed_image, selected_info=info)
   