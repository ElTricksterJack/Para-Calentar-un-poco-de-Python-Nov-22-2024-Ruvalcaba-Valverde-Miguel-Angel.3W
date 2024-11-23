print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------Punto 1---------------")
c = 0
nu = []
while c < 1:#este while te permite ingresar un numero de veces que quieras.
    n = float(input("ingresa un numero:"))
    nu.append(n)#se podria desir que eso permite agregar un elemento a la lista como nuevos valores sin coregir los otros.
    c = int(input("deseas alladir otro numero? 1 si 0 no:"))

def mx(num):#qui esta la funcion
    ma = num[0]#delclara como llaor el primer numero de la lista
    for nume in num:#aqui el nume "filtra" la lista para el siguiente
        if nume > ma:#si hay un numero mayor que ma, pasa al siguiente
            ma = nume#aqui l ambos numeros esta iguale se hasen mayores
    print("Lista de numeros:",num)
    print("El numero mayor es:", ma)
#Nota: tuve que investigar pera haser este codigo
mx(nu)
print("-------------------------------------")
print("Resultado: La funcion funciona funcionalmente bien, hasi que si muestra el numero maximo.\n")
