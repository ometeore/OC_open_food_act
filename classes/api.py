import requests, json

class API:
    """Mise en place et interfaçage d'une base de données MySQL"""

    def __init__(self, url):
        "Établissement de la connexion - Création du curseur"
        parameters = {'json': '1'}
        self.result = requests.get(url , params=parameters )

    def descriptif (self):
        data=content.result.json()
        t=data['products']
        print(t)
        with open('data.json') as json_data:
            print(type(json_data))