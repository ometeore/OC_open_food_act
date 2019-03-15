import json
import requests
from classes.bd import Database
from classes.glob import Glob

class API:
    """Mise en place et interfaçage d'une base de données MySQL"""

    def __init__(self, url, id_categorie):
        "Établissement de la connexion - Création du curseur"
        self.url = url
        self.encoded = requests.get(url).json()
        self.id_categorie = id_categorie



    def description(self):
        """return list of request ready to apply"""

        products = self.encoded['products']     #<-- list
        name_of_product = []
        nutrition_grade_of_product = []
        location_of_product = []
        url_of_product = []
        list_of_request = []

        for product in products:
            try:
                name_of_product.append(product['product_name_fr'])  #<-- list de nom des produits
            except:
                name_of_product.append("NOOOOOOOON")
            try:
                location_of_product.append(product['stores'])
            except:
                location_of_product.append("non disponible")
            url_of_product.append(product['url'])
            nutrition_grade_of_product.append(product['nutrition_grades_tags'][0])
        i = 0
        id_of_aliment = 62
        for name in name_of_product:
            list_of_request.append("INSERT INTO OCOFF_aliments VALUES ('{}','{}', '{}', '{}', 'vide pour le moment', '{}', '{}')".format(j, name, nutrition_grade_of_product[i], self.id_categorie, location_of_product[i], url_of_product[i]))
            i = i + 1
            j = j+1

        return list_of_request

