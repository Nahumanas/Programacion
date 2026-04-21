class PartyAnimal: #Nombre de la clase
    def __init__(self): #metodo
        #self es la isntancia real
        self.x = 0 #define una variable
    
    def party(self): #metodo
        self.x = self.x + 1 
        
        print("So far" , self.x)
#Hasta aqui definimos pero no ejecutamos

an = PartyAnimal()

an.party()
an.party()
an.party()