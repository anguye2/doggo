from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Favorite(MethodView):
    def get(self):
        model = gbmodel.get_model()
        favorite = [dict(id=row[0], name=row[1], weight=row[2], height=row[3],\
            bred_for=row[4], breed_group=row[5], life_span=row[6], temperament=row[7], \
                origin=row[8], date_submitted=row[9], image=row[10]) for row in model.select()]
        return render_template('favorite.html',favorite=favorite)