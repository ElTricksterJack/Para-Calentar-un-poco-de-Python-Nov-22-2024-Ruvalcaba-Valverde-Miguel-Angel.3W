print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------Punto 3---------------")
c = 0
nu = []
while c < 1:#este while te permite ingresar un numero de veces que quieras.
    n = input("ingresa un numero:")
    nu.append(n)#se podria desir que eso permite agregar un elemento a la lista como nuevos valores sin coregir los otros.
    c = int(input("deseas alladir otro numero? 1 si 0 no:"))

def con(e):#agamos una funcion
    cont = 0
    if isinstance(e, (str, list)):  #el if es para que no se repitan los numeros
        for _ in e:#esto permite filtrar
            cont += 1#se podria desir ba contado
    return cont#deblueve el resultado

print("El total de la lista es:",con(nu))
print("-------------------------------------")
print("Resultado: cuenta los elementos de la lista y tambien fienciona con cadenas de texto.\n")
