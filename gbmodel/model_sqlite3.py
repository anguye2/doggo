"""
This is the sqlite database for the Just Dogs flask app
+------+--------------------+-------------+----------+------------+--------------+---------------+--------------+-------------+-----------------+----------------------+
| id   | name               |  weight     | height   |  bred_for  | breed_group  |    life_span  | temperament  |  origin     |  date_submitted |  image               |
+======+====================+=============+==========+============+==============+===============+==============+=========== =+=================+======================+
| 2    | Affenpinscher      |  6 - 13     |9 - 11.5  |   lapdog   |  toy         | 10 - 12 years | Stubborn     | Germany     | 2020-05-10      | https://image.com    |
+------+--------------------+-------------+----------+------------+--------------+---------------+--------------+-------------+-----------------+----------------------+
"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'favorite.db'

class model(Model):
    def __init__(self):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from favorite")
        except sqlite3.OperationalError:
            cursor.execute("create table favorite(id, name, weight, height, bred_for, breed_group, life_span, temperament, origin, date_submitted, image)")
        cursor.close()
    
    def select(self):
        """
        Get all rows from the food cart database
        Each row contains: id, name, weight, height, bred_for, breed_group, life_span, temperament, origin, date_submitted, image
        :return List of lists containg all row of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM favorite")
        return cursor.fetchall()
    
    def insert(self, info):
        # id, name, weight, height, bred_for, breed_group, life_span, temperament, origin, image
        """
        Insert data into the database
        :param id: String
        :param name: String
        :param weight: String
        :param height: String
        :param bred_for: String
        :param breed_group: String
        :param life_span: String
        :param temperament: String
        :param origin: String
        :param date_submitted: String
        :param image: String
        :return: True
        :raises: Database errors on connection and insertion
        """
    
        params = {'id':info[0], 'name':info[1], 'weight':info[2], 'height':info[3], 'bred_for':info[4], 'breed_group':info[5], 'life_span':info[6], 'temperament':info[7], 'origin': info[8], 'date_submitted': date.today(), 'image':info[9]}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into favorite (id, name, weight, height, bred_for, breed_group, life_span, temperament, origin, date_submitted, image) VALUES (:id, :name, :weight, :height, :bred_for, :breed_group, :life_span, :temperament, :origin, :date_submitted, :image)", params)

        connection.commit()
        cursor.close()
        return True
    
