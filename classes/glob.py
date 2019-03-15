class Glob:
    """Espace de noms pour les variables et fonctions <pseudo-globales>"""

    dbName = "OpenClassroom"      # nom de la base de données
    user = "root"              # propriétaire ou utilisateur
    passwd = "marco"            # mot de passe d'accès
    host = "localhost"      # nom ou adresse IP du serveur

    question_initiale = [(1, 1, "Trouver un aliment"),(2, 2, "Retrouver mes aliments substitués.")]
    question_initiale_phrase = "\n\n\nPret à commencer?"
    question_menu_aliment = [
                                (1, 1, "0btenir une présentation de l'aliment"),
                                (2, 2, "Substituer l'aliment"),
                                (3, 3, "Revenir au choix des aliments"),
                                (4, 4,"Revenir au choix des catégories"),
                                (5, 5,"Revenir au menu principal")
                            ]
    question_menu_aliment_phrase = "\n\n\nQue souhaitez vous faire?"
    question_save = [
                        (1, 1, "sauvegarder la substitution en base de donnée"),
                        (2, 2, "revenir au menu principal")
                    ]
    question_save_phrase = "\n\n\nQue souhaitez vous faire?"



    # Structure de la base de données.  Dictionnaire des tables & champs :
    dicoT ={"OCOFF_categories":[('id_categories', "k", "clé primaire"),
                            ('libelle', 50, "nom"),
                            ('lien', 150, "lien vers la catégorie de l'API")],
            "OCOFF_substitution":[('id_aliment', "k", "clé primaire"),
                            ('id_cat', "i", "FK catégorie"),
                            ('descriptif', 3000, "descriptif"),
                            ('lien', 150, "FK lieu de présence du produit")],
            "OCOFF_lieu":[('id', "k", "clé primaire"),
                            ('lieu1', "i", "lieu"),
                            ('lieu2', "i", "lieu"),
                            ('lieu3', "i", "lieu")]}

    

    def print_bouse(self):
        print("bouse")


