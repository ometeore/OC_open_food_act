#####################################################################################
############################UTILISATION DE OPEN FOOD ACTS############################
#####################################################################################


import json, MySQLdb, requests
    
db = MySQLdb.connect(host="localhost",
    user="root",
     passwd="Vendetta7800",      # <--------- vive la discression A metre dans un autre fichier bixon
    db="OpenClassroom")




cur = db.cursor()

cur.execute("SELECT * FROM open_food_act")

for row in cur.fetchall():
    print(row)
 

db.close()
r = requests.get("https://fr.openfoodfacts.org/categories.json")
 
#r -> json  // result -> dictionnaire
result = json.loads(r.text)
#req = requests.request('GET', 'https://world.openfoodfacts.org/api/v0/product/3392460511200.json')
#print(req)

#affiche tout en vrac si décommente
#result1 = result[product][categories_prev_hierarchy]=en:sugary-snacks
print(result)
#print(result)
 

#url="https://world.openfoodfacts.org/api/v0/product/%s.json"(*)
#url="https://fr.openfoodfacts.org/categories.json"
#content=requests.get(url)
#data=content.json()
#t=data['tags']
#print(t[0:20])
#baseDonn = gadfly.gadfly("","")

if __name__ == '__main__':
    def __main__():
        """     Ceci est le main"""
        continuer_choix = True
        while continuer_choix:
            print("****")
            print("****")
            print("****")
            print("1. Quel aliment souhaitez vous remplacer?")
            print("2. Retrouvez les aliments que vous souhaitez substituer.")
            continuer_choix = input("             Que voulez vous faire?")
            if continuer_choix == "1":
                print("****") 
                print("Sélectionnez la catégorie")
                print("****") 
            else:
                print("****") 
                print("coucou maman :).")
                print("****") 

    __main__()
