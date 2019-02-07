import MySQLdb
from glob import *

class Database:
    """Mise en place et interfaçage d'une base de données MySQL"""

    def __init__(self, dbName, user, passwd, host):
        "Établissement de la connexion - Création du curseur"

        try:
            self.baseDonn = MySQLdb.connect(db =dbName,
                  user =user, passwd =passwd, host =host)

        except Exception:
            print ('La connexion avec la base de données a échoué :\n'\
                  'Erreur détectée :\n')
            self.echec =1

        else:    
            self.cursor = self.baseDonn.cursor()   # création du curseur
            self.echec =0


    def executer_req(self, req):
        "Exécution de la requête <req>, avec détection d'erreur éventuelle"
        try:
            self.cursor.execute(req)
            return 1
        except Exception:
            #afficher la requête et le message d'erreur système :
            print ("Requête SQL incorrecte :\n%s\nErreur détectée :\n"\
                   % (req))
            return 0
        else:
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
