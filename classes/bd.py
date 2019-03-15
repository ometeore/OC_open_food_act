import MySQLdb
from glob import *
from classes.product import Product
from classes.validateur_de_texte import Text_control
from classes.glob import Glob

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
        i = 1
        for record in records:
            morceau = []
            morceau.append(i)
            morceau.append(record[0])
            morceau.append(record[1])
            char.append(morceau)
            i = i + 1
        return char

    def print_list_aliment(self, categorie):
        """ retourne la liste d'aliment de la bonne categorie sous forme de liste de liste"""
        requete = "SELECT * FROM OCOFF_aliments WHERE categorie = {}".format(categorie)
        self.executer_req(requete)
        records = self.resultat_req_all()
        char = []
        i = 1
        for record in records:
            morceau = []
            morceau.append(i)
            morceau.append(record[0])
            morceau.append(record[1])
            char.append(morceau)
            i = i + 1
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
        """ retourne une liste de liste [[element mauvais, bon element], ...]"""
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

    def print_the_substitution(self):
        """affiche les substitutions"""
        block=[]
        block = self.presentation_of_substitute()
        if block == []:
            print("\n\n\nVous n'avez pas encore substituer d'aliments.")
        else:
            for substitution in block:
                aliment_bad = Product(self, substitution[0])
                aliment_bad.hydrate_aliment()
                aliment_good = Product(self, substitution[1])
                aliment_good.hydrate_aliment()
                self.presentation_substitution(aliment_bad, aliment_good)
    
    def the_save_choice_scenario(self, user_aliment_choice):

        aliment = Product(self, user_aliment_choice)
        aliment.hydrate_aliment()
        aliment_good = Product(self, self.substitute_aliment(aliment))
        aliment_good.hydrate_aliment()
        self.presentation_substitution(aliment, aliment_good)

        user_save_choice = True
        # user is in save choice menu
        while user_save_choice:
            save_or_not = Text_control(Glob.question_save, Glob.question_save_phrase)
            save = save_or_not.question()
            if save == 1:
                self.save_substitute(aliment.id, aliment_good.id)
                user_save_choice = False

            else:
                user_save_choice = False

    def what_to_do_with_aliment_choice(self, user_aliment_choice):
        user_choose_what_to_do_with_aliment = True
        while user_choose_what_to_do_with_aliment:
            what_to_do = Text_control(Glob.question_menu_aliment, Glob.question_menu_aliment_phrase)
            result = what_to_do.question()
            if result == 1:
                aliment = Product(self, user_aliment_choice)
                aliment.hydrate_aliment()
                aliment.presentation()
            if result == 2:
                self.the_save_choice_scenario(user_aliment_choice)
                [user_choose_what_to_do_with_aliment,user_aliment_choice, user_categori_choice] = [False, False, False]

            if result == 3:
                user_choose_what_to_do_with_aliment = False
            if result == 4:
                [user_choose_what_to_do_with_aliment, user_aliment_choice] = [False, False]
            if result == 5:
                [user_choose_what_to_do_with_aliment, user_aliment_choice, user_categori_choice] = [False, False, False]