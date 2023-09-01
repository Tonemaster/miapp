"""def funcion_suma(n1,n2):
    print(n1+n2)

funcion_suma(4,5)

def cuenta_hacia_tras(numero):
    numero-=1
    if(numero>0):
        print("vamos en el numero: ", numero)
        cuenta_hacia_tras(numero)
    else:
        print("terminamos")

numero_ingresado = int(input("DIGITE UN NUMERO: "))
cuenta_hacia_tras(numero_ingresado) """

def factorial(numero):
    if(numero>1):
        numero=numero*factorial(numero - 1)
    return numero
    
print(factorial(5))