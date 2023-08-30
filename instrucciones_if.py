var_entrada=input("Digite su edad: ")
var_edad=int(var_entrada)
if(var_edad<0):
    print("la edad es incorrecta, no puede ser negativa.")
elif(var_edad<=0):
    print("la edad es incorrecta y debe ser mayor a cero.")
elif(var_edad>0 and var_edad<18):
    print("Menor de edad.")
else:
    print("Es mayor de edad.")