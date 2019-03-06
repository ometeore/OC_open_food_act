
class Text_control:
    """Mise en place et interfaçage d'une base de données MySQL"""
    def __init__(self, data_group, chaine):
        self.data = data_group
        self.chaine = chaine



    def presentation(self): 
        print (self.chaine)
        print("\n\n Les choix disponibles sont:\n ")
        for element in self.data:
            print("{} : {}".format(element[0],element[2]))

    def question(self):
        self.presentation()
        user_wrong_answer = True
        while user_wrong_answer:
            question = input("")
            
            try:
                question = int(question)
                for element in self.data:
                    if question == element[0]:
                        user_wrong_answer = False
                        reponse = element[1]
                if user_wrong_answer:
                    print("not in list")
                 
            except: 
                if question == "X":
                    return None

                print("fail")
        return reponse
        




