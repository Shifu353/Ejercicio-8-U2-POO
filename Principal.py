if __name__ == '__main__':
    from Clase_Conjunto import Conjunto
    def Cargar (num):
        Lista=[]
        print("A continuacion ingrese numero entero para el Conjunto {} y finalice con Fin".format(num))
        valor=input("Ingrese el valor o termine con Fin: ")
        while(valor!="fin"):
            valor=int(valor)
            if(type(valor)==int):
                Lista.append(valor)
            else:
                print("Tipo de valor INCORRECTO")
                valor=input("Ingrese el valor o termine con Fin: ")
            valor=input("Ingrese el valor o termine con Fin: ")
            if type(valor) == str:
                valor = valor.lower()

        Lista=list(set(Lista))
        return Conjunto(Lista)
    def op1 (Primer_conjunto):
        print("Por favor ingrese un segundo Conjunto")
        Segundo_Conjunto=Cargar("B")
        resultado=Primer_conjunto+Segundo_Conjunto
        print("Resultado de la Union",resultado)
        input("Precione enter para continuar....")
    def op2 (Primer_conjunto):
        print("Por favor ingrese un segundo Conjunto")
        Segundo_Conjunto=Cargar("B")
        resultado=Primer_conjunto  - Segundo_Conjunto
        print("Resultado de la diferecncia: ",resultado)
        input("Precione Enter para continuar....")
    
    def op3 (Primer_conjunto):
        print("Por favor ingrese un segundo Conjunto")
        Segundo_Conjunto=Cargar("B")
        Primer_conjunto == Segundo_Conjunto
        input="Precione Enter para Continuar...."
    
    def op4 ():
        print("Saliendo del Programa...")
    
    Primer_conjunto = Cargar("A")
    
    opcion=None
    diccionario={1:op1,2:op2,3:op3,4:op4}
    while(opcion!=4):
        print("\n")
        print("|------------------------Menu---------------------------|")
        print("| Ingrese 1 para la union de dos Conjuntos              |")
        print("| Ingrese 2 para la diferecia de dos Conjuntos          |")
        print("| Ingrese 3 para verificar si dos Conjuntos son iguales |")
        print("| Ingrese 4 para salir del programa                     |")
        print("|-------------------------------------------------------|")
        opcion=int(input("Ingrese Opcion: \n"))
        op=diccionario.get(opcion,lambda: print("Opcion Incorrecta"))
        if op == 4:
            op()
        else:
            op(Primer_conjunto)
