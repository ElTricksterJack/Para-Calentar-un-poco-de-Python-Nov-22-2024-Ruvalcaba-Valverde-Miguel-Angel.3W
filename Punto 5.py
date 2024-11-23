print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------Punto 5---------------")
c = 0
nu = []
while c < 1:#este while te permite ingresar un numero de veces que quieras.
    n = float(input("ingresa un numero:"))
    nu.append(n)#se podria desir que eso permite agregar un elemento a la lista como nuevos valores sin coregir los otros.
    c = int(input("deseas alladir otro numero? 1 si 0 no:"))
def sum(num):#creamos una funcion
    r = 0#creamos una nueva bariable
    for nume in num:#hasemos un bucle
        r += nume#hasemos que cada elemento de la lista se sume al actual
    print("Resultado de la suma: ",r)#mostrar la suma total
def mul(num):#aqui sigue siendo el mismo proseso.
    r = 1 #Nota: la primera version embes de 1 era 0, y dio error porque no se puede multiplicar por 0
    for nume in num:
        r *= nume
    print("Resultado de la multiplicasion: ",r)
print("Lista: ",nu)#ahora solo se muestra la lista y se invoca las funciones.
sum(nu)
mul(nu)
print("--------------------------------------")
print("Resultado: se logra ver los resultados y funciono.\n")
