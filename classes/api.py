import requests, json

class API:
    """Mise en place et interfaçage d'une base de données MySQL"""

    def __init__(self, url):
        "Établissement de la connexion - Création du curseur"
        self.encoded = requests.get(url)
        self.decoded = self.encoded.json()
        self.url = url

    def description (self):
                    # v-- JSON
        print(self.url)
        print(self.decoded)  
        #print(self.decoded['products']['product_name'])
        #print(self.decoded[products])
        #print(self.decoded[products][nutrient_levels])
        #for key, value in self.decoded['products'].iteritems():
            #print (key, value)