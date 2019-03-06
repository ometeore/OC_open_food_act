import MySQLdb
from glob import *
from classes.product import Product

class Database:
    """Mise en place et interfaçage d'une base de données MySQL"""
    def __init__(self, dbName, user, passwd, host):
        "Établissement de la connexion - Création du curseur"
        try:
            self.baseDonn = MySQLdb.connect(db=dbName, user=user, passwd=passwd, host=host)
        except Exception as err:
            print('La connexion avec la base de données a échoué :\n'\
                  'Erreur détectée :\n%s ' %err)
            self.echec = 1
        else:
            self.cursor = self.baseDonn.cursor()   # création du curseur
            self.echec = 0

    def executer_req(self, req):
        """Exécution de la requête <req>, avec détection d'erreur éventuelle"""
        self.cursor.execute(req)
        return 1

    def resultat_req_all(self):
        """renvoie le résultat de la requête précédente (un tuple de tuples)"""
        return self.cursor.fetchall()

    def resultat_req_one(self):
        """renvoie le résultat de la requête précédente (un tuple de tuples)"""
        return self.cursor.fetchone()

    def close(self):
        """ debloque le curseur """
        if self.baseDonn:
            self.baseDonn.close()

    def print_the_categori(self):
        # selection_categori of the cathegorie
        self.executer_req("SELECT * FROM OCOFF_categories")
        # analyser le résultat de la requête ci-dessus :
        records = self.resultat_req_all()      # ce sera un tuple de tuples
        char = []
        for record in records:
            morceau = []
            morceau.append(record[0])
            morceau.append(record[1])
            char.append(morceau)
        return char

    def print_list_aliment(self, categorie):
        """ retourne la liste d'aliment de la bonne categorie sous forme de liste de liste"""
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
        """ va chercher un aliment de meilleur capacité nutritionelle de même catégorie"""
        requete = "SELECT * FROM OCOFF_aliments WHERE categorie = {}".format(aliment.categorie)
        self.executer_req(requete)
        result = 0
        temp_grade = aliment.grade
        aliments_substituables = self.resultat_req_all()
        for aliments in aliments_substituables:
            if temp_grade > aliments[2]:
                temp_grade = aliments[2]
                result = aliments[0]
        if result == 0:
            return aliment.id
        return result

    def presentation_substitution(self, aliment_bad, aliment_good):
        """ print le resultat de la substitution"""
        if aliment_bad.id == aliment_good.id:
            print("\n\n\nvotre aliment a déja la meilleur note nutritionelle possible pour sa catégorie")
        else:
            print("\n\nnous vous proposons de remplacer:")
            aliment_bad.presentation()
            print("\npar:")
            aliment_good.presentation()

    def save_substitute(self, id1, id2):
        """ sauvegarde en base de donnée l'élemnt substitué ainsi que le résultat de la substitution"""
        requete = "INSERT INTO OCOFF_substitution VALUES ({},{})".format(id1, id2)
        try:
            self.executer_req(requete)
            self.baseDonn.commit()
            print("\n\n\nl'aliment a été sauvegardés.")
        except:
            print("\n\n\nl'aliment à déjà été substitué.  Allez voir dans mes alliments substitués dans la base de donnée")

    def presentation_of_substitute(self):
        self.executer_req("SELECT * FROM OCOFF_substitution")
        # analyser le résultat de la requête ci-dessus :
        records = self.resultat_req_all()      # ce sera un tuple de tuples
        char = []
        for record in records:
            morceau = []
            morceau.append(record[0])
            morceau.append(record[1])
            char.append(morceau)
        return char