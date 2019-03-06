#####################################################################################
########################### USE OF THE API OPEN FOOD ACTS ###########################
###########################  LOCALHOST AND SQL REQUESTS   ###########################
#####################################################################################


from classes.bd import Database
from classes.glob import Glob
from classes.api import API
from classes.product import Product
from classes.validateur_de_texte import Text_control





if __name__ == '__main__':
    def __main__():
        """Hello world"""

        # Creation of the object wich connect to database :
        bd = Database(Glob.dbName, Glob.user, Glob.passwd, Glob.host)

        user_initial_choice = True
        while user_initial_choice:

            # Initial user choice select replacement of aliments already replace or choice of a new aliment
            initial_choice = Text_control(
                [
                    (1, "Trouver un aliment"),
                    (2, "Retrouver mes aliments substitués.")
                ],
                "Bonjour"
            )
            user_initial_choice = initial_choice.question()
            if user_initial_choice == 1:

                # user is in categori choice
                user_categori_choice = True
                while user_categori_choice:
                    categori_choice = Text_control(
                        bd.print_the_categori(),
                        "\n\n\n****\nSélectionnez la catégorie\n****"
                    )
                    bd.print_the_categori()
                    user_categori_choice = categori_choice.question()
                    #user can choose what he want to do with an aliment
                    user_aliment_choice = True
                    while user_aliment_choice:
                        aliment_choice = Text_control(
                            bd.print_list_aliment(user_categori_choice),
                            "\n\n\n\nQuel aliment choisissez vous?"
                        )


                        user_aliment_choice = aliment_choice.question()

                        user_choose_what_to_do_with_aliment = True
                        while user_choose_what_to_do_with_aliment:
                            what_to_do = Text_control(
                                [
                                    (1, "obtenir une présentation de l'aliment"),
                                    (2, "substituer l'aliment"),
                                    (3, "Revenir au choix des aliments"),
                                    (4, "revenir au choix des catégories"),
                                    (5, "revenir au menu principal")
                                ],
                                "\n\n\nQue souhaitez vous faire?"
                            )
                            result = what_to_do.question()
                            if result == 1:
                                aliment = Product(bd, user_aliment_choice)
                                aliment.hydrate_aliment()
                                aliment.presentation()
                            if result == 2:
                                aliment = Product(bd, user_aliment_choice)
                                aliment.hydrate_aliment()
                                aliment_good = Product(bd, bd.substitute_aliment(aliment))
                                aliment_good.hydrate_aliment()
                                bd.presentation_substitution(aliment, aliment_good)

                                user_save_choice = True
                                while user_save_choice:
                                    save_or_not = Text_control(
                                        [
                                            (1, "sauvegarder la substitution en base de donnée"),
                                            (2, "revenir au menu principal")
                                        ],
                                        "\n\n\n Que souhaitez vous faire?"
                                    )
                                    save = save_or_not.question()
                                    if save == 1:
                                        bd.save_substitute(aliment.id, aliment_good.id)
                                        user_save_choice = False
                                        user_choose_what_to_do_with_aliment = False
                                        user_aliment_choice = False
                                        user_categori_choice = False
                                    else:
                                        user_save_choice = False
                                        user_choose_what_to_do_with_aliment = False
                                        user_aliment_choice = False
                                        user_categori_choice = False


                            if result == 3:
                                user_choose_what_to_do_with_aliment = False
                            if result == 4:
                                user_choose_what_to_do_with_aliment = False
                                user_aliment_choice = False
                            if result == 5:
                                user_choose_what_to_do_with_aliment = False
                                user_aliment_choice = False
                                user_categori_choice = False






# print the result of the API research
                    #content = API(url, user_categori_choice)
                    #content.description()


            else:
            # find product already substitute
                block=[]
                block = bd.presentation_of_substitute()
                print(block)
                for substitution in block:
                    aliment_bad = Product(bd, substitution[0])
                    aliment_bad.hydrate_aliment()
                    aliment_good = Product(bd, substitution[1])
                    aliment_good.hydrate_aliment()
                    bd.presentation_substitution(aliment_bad, aliment_good)

        bd.close()

__main__()
