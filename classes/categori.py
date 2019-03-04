#une catégorie a son lien propre, son nombre d'élément,
#ainsi qu'une liste de lien vers ses produits

from classes.bd import Database

class Categorie:
    """Récupération et utilisation d'une catégorie"""

    def __init__(self, url):
        self.url = url
        self.encoded = requests.get(url).json()
        self.products = self.encoded['products']
