class Enregistreur:
    """classe pour gérer l'entrée d'enregistrements divers"""

    def __init__(self, bd, table):
        self.bd =bd
        self.table =table
        self.descriptif =Glob.dicoT[table]   # descriptif des champs


    def entrer(self):
        "procédure d'entrée d'un enregistrement entier"
        champs ="("           # ébauche de chaîne pour les noms de champs
        valeurs ="("          # ébauche de chaîne pour les valeurs
        # Demander successivement une valeur pour chaque champ :
        for cha, type, nom in self.descriptif:
            if type =="k":    # on ne demandera pas le n° d'enregistrement
                continue      # à l'utilisateur (numérotation auto.)
            champs = champs + cha + ","
            val = raw_input("Entrez le champ %s :" % nom)
            if type =="i":
                valeurs = valeurs + val +","
            else:
                valeurs = valeurs + "'%s'," % (val)


        champs = champs[:-1] + ")"    # supprimer la dernière virgule,
        valeurs = valeurs[:-1] + ")"  # ajouter une parenthèse
        req ="INSERT INTO %s %s VALUES %s" % (self.table, champs, valeurs)
        self.bd.executerReq(req)

        ch =raw_input("Continuer (O/N) ? ")
        if ch.upper() == "O":
            return 0
        else:
            return 1