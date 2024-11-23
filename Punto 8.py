print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Punto 8---------------")
def comp(un):#creamos una funcion
    repe = []#hasemos un par de variables
    repet = False
    under = ("unseen", "unfede", "untell", "unrepair", "undecrease", "untrust", "unback", "undraw", "unburn", "unchaste", "unluck", "unfair")
    #que comiense el show
    for i in range(len(un)):#Verificamos los elementos de un contra los de under
        for q in range(len(under)):#ahora verificamos los elementos de under contra los de un
            if un[i] == under[q]:#despues bemos si hay elementos iguales
                repe.append(un[i])#luego los agregamos a repe
                repet = True#y le damos el valor true a repat

    print("-------------------------------------")
    if repet:#ahora si hay un negador repetido dentro de la lista de alladida de un en la lista under saldra esto.
        print("los Negadores que an estado en ambas organisaciones son:", repe)
        print(bool(repet))#aqui comprobamos su valor
    else:
        print("No hay Negadores que estubieran en ambas organisaciones.")
        print(bool(repet))

union = ("undead", "unluck", "unfeel", "unmove", "unfair", "untouchable", "unstoppable", "untruth", "unavoidable", "unchange", "unjustice", "unbreakable", "unforgettable")
#hay union como quiero undead unluck
print("Apocalipsis que miebros formaron parte de under y la union")
comp(union)#invocacion de la funcion

print("-------------------------------------")
print("Resultado: se ve si hay algun elemento repetido.\n")
