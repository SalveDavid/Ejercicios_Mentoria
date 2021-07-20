# Encontrar si dos cadenas de texto son anagramas.
# Crear una funcion en que recibe 2 cadenas de texto como parametro
# Debe devolver true o false
# Ejemplo:
# anim al a n imal
# lamin a l amina

def ordenamiento(texto):
    lista = list(texto)
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = aux
    return lista


def anagrama(texto1, texto2):

    return "".join(ordenamiento(texto1)) == "".join(ordenamiento(texto2))


print(anagrama(input("Ingrese cadena1: ").replace(" ", "").lower(), input("Ingrese cadena2: ").replace(" ", "").lower()))
