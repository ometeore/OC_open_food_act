import MySQLdb
from glob import *
from classes.product import Product

class Database:
    """Mise en place et interfaçage d'une base de données MySQL"""
    def __init__(self, dbName, user, passwd, host):
        "Établissement de la connexion - Création du curseur"
        try:
            self.baseDonn = MySQLdb.connect(db =dbName,
                  user =user, passwd =passwd, host =host)
        except Exception as err:
            print ('La connexion avec la base de données a échoué :\n'\
                  'Erreur détectée :\n%s ' %err)
            self.echec =1
        else:    
            self.cursor = self.baseDonn.cursor()   # création du curseur
            self.echec =0

    def executer_req(self, req):
        "Exécution de la requête <req>, avec détection d'erreur éventuelle"
        self.cursor.execute(req)
        return 1

    def resultat_req_all(self):
        "renvoie le résultat de la requête précédente (un tuple de tuples)"
        return self.cursor.fetchall()

    def resultat_req_one(self):
        "renvoie le résultat de la requête précédente (un tuple de tuples)"
        return self.cursor.fetchone()        

    def close(self):
        if self.baseDonn:
            self.baseDonn.close()

    def print_the_categori(self):
        # selection_categori of the cathegorie                         
        self.executer_req("SELECT * FROM OCOFF_categories")
        # analyser le résultat de la requête ci-dessus :
        records = self.resultat_req_all()      # ce sera un tuple de tuples

        #construction d'une liste de categorie en fonction de ce qui trouver dans la base
        for row in records:            # => chaque champ dans l'enreg.
            print("Tapez {} pour {}".format(row[0],row[1]))
        print("***\n")



    def print_list_aliment(self, categorie):
        requete = "SELECT * FROM OCOFF_aliments WHERE categorie = {}".format(categorie)
        self.executer_req(requete)
        records = self.resultat_req_all()
        char = []
        for record in records:
            morceau = []
            morceau.append(record[0])
            morceau.append(record[1])
            char.append(morceau)
        return char
    
    def substitute_aliment(self, aliment):
        pass












