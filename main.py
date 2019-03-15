#####################################################################################
########################### USE OF THE API OPEN FOOD ACTS ###########################
###########################  LOCALHOST AND SQL REQUESTS   ###########################
#####################################################################################

from classes.glob import Glob
from classes.bd import Database
from classes.api import API
from classes.product import Product
from classes.validateur_de_texte import Text_control


if __name__ == '__main__':
    def main():
        """Hello world"""

        bd = Database(Glob.dbName, Glob.user, Glob.passwd, Glob.host)
        user_initial_choice = True
        
        # Initial user choice select replacement of aliments already replace or choice of a new aliment
        while user_initial_choice:
            Glob.question_initiale
            initial_choice = Text_control(Glob. question_initiale, Glob.question_initiale_phrase)
            user_initial_choice = initial_choice.question()
            if user_initial_choice == 1:

                # user is in categori choice
                user_categori_choice = True
                while user_categori_choice:
                    categori_choice = Text_control(bd.print_the_categori(), "\n\n\n****\nSélectionnez la catégorie\n****")
                    user_categori_choice = categori_choice.question()      
                    user_aliment_choice = True
                    
                    # user is in aliment choice menu
                    while user_aliment_choice:
                        aliment_choice = Text_control(bd.print_list_aliment(user_categori_choice),"\n\n\nQuel aliment choisissez vous?")
                        user_aliment_choice = aliment_choice.question() 
                        # user choose what to do with
                        bd.what_to_do_with_aliment_choice(user_aliment_choice)

            else:
            # find product already substitute and print them
                bd.print_the_substitution()

        bd.close()

main()
