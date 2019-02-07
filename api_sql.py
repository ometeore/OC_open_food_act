#####################################################################################
########################### USE OF THE API OPEN FOOD ACTS ###########################
#####################################################################################

from classes.bd import Database
from classes.glob import Glob
from classes.api import API

question = "****\n****\n****\n1. Quel aliment souhaitez vous remplacer?\n2. Retrouver mes aliments substitués.\n"
selection = "****\nSélectionnez la catégorie\n****"

if __name__ == '__main__':
    def __main__():
        """Hello world"""
        
        # Creation of the object wich connect to database : 
        bd = Database(Glob.dbName, Glob.user, Glob.passwd, Glob.host)
        user_choice = True
        while user_choice:

# Initial user choice
            print(question)
            user_choice = input("             Que voulez vous faire?")
            if user_choice == "1":
                user_choice_0 = True
                while user_choice_0:
                    user_choice_0 = False
                    print(selection)
             
# Selection of the cathegorie                    

                    if bd.executer_req("SELECT * FROM OCOFF_categories"):
                    # analyser le résultat de la requête ci-dessus :
                        records = bd.resultat_req_all()      # ce sera un tuple de tuples
                        for row in records:            # => chaque champ dans l'enreg.
                            print("Tapez {} pour {}".format(row[0],row[1])),

                    user_choice_0 = input("             Quel catégorie choisissez vous?") 
                    test = user_choice_0
                    try:
                        user_choice_0 = int(user_choice_0)
                    except ValueError:
                        print("boom")


# find the url 
                    requete = 'SELECT lien FROM OCOFF_categories WHERE id_categories =' + test
                    
#il faut tester contre une insertion sql



                    if bd.executer_req(requete):
                    # analyser le résultat de la requête ci-dessus :
                        records = bd.resultat_req_one()      # ce sera un tuple de tuples
                        url = records[0]
                    
                    content = API(url)
                    content.description()
                    bd.close()         
# creer une table specifique pour ca            
                
            else:
                print("****")
                print("coucou maman :).")
                print("****")

__main__()
