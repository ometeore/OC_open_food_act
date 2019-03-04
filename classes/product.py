#un produit à son lien propre, son nom, ses lieus d'achats + cf énoncé


class Product:
    """Récupération et utilisation d'une catégorie"""

    def __init__(self,db ,id=0, name="", grade="", categorie="", description="",location="", url=""):
        self.db = db
        self.id = id
        self.name = name
        self.grade = grade
        self.categorie = categorie
        self.description = description
        self.location = location
        self.url = url


    def presentation(self):
        print("\n****\nname: {},\nnutritional grade: {},\ndescription: {},\npoint de vente: {},\nurl: {}\n****\n".format(self.name, self.grade, self.description, self.location, self.url))

    


    def hydrate_aliment(self):
        #liste pour hydrater aliment ------ id, name, grade, categorie, description,location, url
        requete = "SELECT * FROM OCOFF_aliments WHERE id_aliment = {}".format(self.id)
        self.db.executer_req(requete)
        records = self.db.resultat_req_one()
        self.name = records[1]
        self.grade = records[2]
        self.categorie = records[3]
        self.description = records[4]
        self.location = records[5]
        self.url = records[6]
        
        

