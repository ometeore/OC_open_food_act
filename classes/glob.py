class Glob:
    """Espace de noms pour les variables et fonctions <pseudo-globales>"""

    dbName = "OpenClassroom"      # nom de la base de données
    user = "root"              # propriétaire ou utilisateur
    passwd = "marco"            # mot de passe d'accès
    host = "localhost"      # nom ou adresse IP du serveur

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


question = "****\n****\n****\n1. Quel aliment souhaitez vous remplacer?\n2. Retrouver mes aliments substitués.\n"
selection = "****\nSélectionnez la catégorie\n****"