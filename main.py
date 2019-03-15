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
                        user_choose_what_to_do_with_aliment = True
                        
                        # user choose what to do with aliment
                        while user_choose_what_to_do_with_aliment:
                            what_to_do = Text_control(Glob.question_menu_aliment, Glob.question_menu_aliment_phrase)
                            result = what_to_do.question()
                            if result == 1:
                                aliment = Product(bd, user_aliment_choice)
                                aliment.hydrate_aliment()
                                aliment.presentation()
                            if result == 2:
                                bd.the_save_choice_scenario(user_aliment_choice)
                                [user_choose_what_to_do_with_aliment,user_aliment_choice, user_categori_choice] = [False, False, False]

                            if result == 3:
                                user_choose_what_to_do_with_aliment = False
                            if result == 4:
                                user_choose_what_to_do_with_aliment = False
                                user_aliment_choice = False
                            if result == 5:
                                user_choose_what_to_do_with_aliment = False
                                user_aliment_choice = False
                                user_categori_choice = False

            else:
            # find product already substitute and print them
                bd.print_the_substitution()

        bd.close()

main()
