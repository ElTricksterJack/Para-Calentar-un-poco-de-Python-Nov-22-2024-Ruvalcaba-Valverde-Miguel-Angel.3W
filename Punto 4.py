print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------Punto 4---------------")
car = input("una letra porfavor: ").lower()#primero capturamos el dato, y el lower se encarga de que el resultado se leea en minuscula y mayuscula.
def esv(c):
    if c == "a" or c == "e" or c == "i" or c == "o" or c== "u":#probabilidades de true
        return True#debuelve true
    else:
        return False#lo mismo pero con false
print("si es true es vocal y si el false no es volcal: ",esv(car))#mostrar resultado
print("-------------------------------------")
print("Resultado: si sirve.\n")
