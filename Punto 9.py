print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Punto 9---------------")
def gecar(n):#creamos la funcion
    res = ""#este valor es como un almase para sumar el resutlado
    for _ in range(n):#qui el for se repite n veces grasias al range sin nesesidad de un valor, grasias al _
        res += " ♠ "#aqui se ban acumulando las pikas
    print(res)#y aqui se imprime el resultado
g = int(input("Ingrese un numero *ENTERO*: "))#capturar dato
gecar(g)#invocamos la funcion
print("-------------------------------------")
print("Resultado: se repite la pika las veses espesificadas.\n")
