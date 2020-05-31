import requests
import random

INFO_API_KEY = "ca91e3a6-8784-491e-ade7-19e6b0e6d5cc"
info_url = "https://api.thedogapi.com/v1/"
photo_url = "https://dog.ceo/api/"

def get_breed():
    """
    Get a list of breeds from into_url
    Output: a dictionary of breeds with key=bread_id, value=breed_name
    """
    url = info_url + "breeds?apiKey=" + str(INFO_API_KEY)
    ret = requests.get(url=url)
    data = ret.json()
    breeds = {}     # dict. of breeds name to display on dropdowns
    for i in data:
        breeds[i['id']]=i['name'].lower()
    return breeds

def get_breed_info(id):
    """
    Get information of a specific breed
    Input: breed id 
    Output: a list of dictionary
    """
    url_info = info_url + "breeds/" + str(id) + "?apiKey" + INFO_API_KEY
    ret = requests.get(url=url_info)
    data_info = ret.json()
    return data_info

def bread_photo(selected_breed):
    url = photo_url + "breeds/list/all"
    ret = requests.get(url=url)
    data = ret.json()
    breeds = data['message']
    keys = list(breeds.keys())
    l = []
    for i in keys:
        l.append(i)
    for i in l:
        if i in selected_breed.lower():
            return i
    
def get_photo(breed):
    """
    Get photos of a chosen breed
    Input: name of a breed
    Output: photos' urls
    """
    breed_name = bread_photo(breed)
    if breed_name is None:
        url_photo = photo_url + "breeds/image/random" 
        ret = requests.get(url=url_photo)
        data_photo = ret.json()
        photo = data_photo['message']
        return photo
    else:
        url_photo = photo_url + "breed/" + str(breed_name) + "/images"
        ret = requests.get(url=url_photo)
        data_photo = ret.json()
        length = len(data_photo['message'])
        rand = random.randint(0,length)
        photo = data_photo['message'][rand]
       
        return photo

# Take all the infomation and put in a list for database in order 
# id, name, weight, height, bred_for, breed_group, life_span, temperament, origin, image
def db_info(info, photo):
        """
        {'weight': {'imperial': '6 - 13', 'metric': '3 - 6'}, 
        'height': {'imperial': '9 - 11.5', 'metric': '23 - 29'}, 
        'id': 1, 
        'name': 'Affenpinscher', 
        'bred_for': 'Small rodent hunting, lapdog', 
        'breed_group': 'Toy',
        'life_span': '10 - 12 years', 
        'temperament': 'Stubborn, Curious, Playful, Adventurous, Active, Fun-loving', 
        'origin': 'Germany, France'}
        """
        keys = ['id', 'name', 'weight', 'height', 'bred_for', 'breed_group', 'life_span', 'temperament', 'origin']

        # Not all breeds have all the key info so make sure to fill them in w empty string
        for i in keys:
            if i not in info.keys():
                info[i]= ''
        try:
            ret = info['id'], info['name'], info['weight']['imperial'], info['height']['imperial'],\
                info['bred_for'], info['breed_group'], info['life_span'], info['temperament'], info['origin'], photo
            return ret
        except KeyError:
            pass

# Info to display on web
def info(breed_name):
    breeds = get_breed()                                                  
    breed_id = list(breeds.keys())[list(breeds.values()).index(breed_name)]
    info =  get_breed_info(breed_id)                                                                                              #                  
    photo = get_photo(breed_name)
    return breeds, info, photo