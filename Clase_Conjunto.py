class Conjunto ():
    __ListaConjuntos = []

    def __init__ (self,lista):
        self.__ListaConjuntos = lista
    
    def MostrarLista (self):
        print(self.__ListaConjuntos)

    def getConjunto (self):
        return self.__ListaConjuntos
    
    def __add__ (self,union):
        nueva=[]
        nueva.extend(self.__ListaConjuntos)
        nueva.extend(union.getConjunto())
        nueva = set(nueva)
        return nueva
    
    def __sub__ (self,resta):
        lista = []
        lista.extend(self.__ListaConjuntos)
        conjunto = resta.getConjunto()
        for valor in conjunto:
            if valor in lista:
                lista.remove(valor)
        return lista
    
    def __eq__ (self,conju):
        conjunto=conju.getConjunto()
        a=len(self.__ListaConjuntos)
        b=len(conjunto)
        if a == b:
            i=0
            while(i<b and conjunto[i]==self.__ListaConjuntos[i]):
                i+=1
            if(i==a):
                print("Los Conjuntos son iguales")
                print("Conjunto 1: ",self.__ListaConjuntos)
                print("Conjunto 2: ",conjunto)
            else:
                print("Las listas son distintas")
                print("Conjunto 1: ",self.__ListaConjuntos)
                print("Conjunto 2: ",conjunto)
        else:
            print("Las listas son distintas")
            print("Conjunto 1: ",self.__ListaConjuntos)
            print("Conjunto 2: ",conjunto)
