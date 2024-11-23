print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Punto 10---------------")
def hiso(p):#creamos una funcion
    for n in p:#p se repite cuantos numeros tenga la lista
        print(f"{n}| {"▓" * n}")#aui en la primera parte se coloca un numero de la lista y luego se multiplica el numero de la lista por el numero.
c = 0
nu = []
while c < 1:#este while te permite ingresar un numero de veces que quieras.
    ne = int(input("ingresa un numero:"))#nota tube que poner esto como int ya que altes salia como error.
    nu.append(ne)#se podria desir que eso permite agregar un elemento a la lista como nuevos valores sin coregir los otros.
    c = int(input("deseas alladir otro numero? 1 si 0 no:"))
hiso(nu)
print("-------------------------------------")
print("Resultado: se puede crear un histograma fasilente.\n")
