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
        """print request ready to apply"""

        products = self.encoded['products']     #<-- list
        name_of_product = []
        nutrition_grade_of_product = []
        location_of_product = []
        url_of_product = []
        list_of_request = []
        #for cle in self.encoded['products'][0].keys():
        #    print (cle)
        for product in products:
            name_of_product.append(product['product_name_fr'])  #<-- list de nom des produits
            nutrition_grade_of_product.append(product['nutrition_grades_tags'][0])
            location_of_product.append(product['stores'])
            url_of_product.append(product['url'])



        i = 0
        j = 14
        for name in name_of_product:
            list_of_request.append("INSERT INTO OCOFF_aliments VALUES ('{}','{}', '{}', '{}', 'vide pour le moment', '{}', '{}')".format(j, name, nutrition_grade_of_product[i], self.id_categorie, location_of_product[i], url_of_product[i]))
            i = i + 1
            j = j+1

        bd = Database(Glob.dbName, Glob.user, Glob.passwd, Glob.host)
        for requete in list_of_request:
            print(requete)

        bd.close()
