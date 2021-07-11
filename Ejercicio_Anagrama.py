# Encontrar si dos cadenas de texto son anagramas.
# Crear una funcion en que recibe 2 cadenas de texto como parametro
# Debe devolver true o false
# Ejemplo:
# anim al a n imal
# lamin a l amina

def ordenamiento(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = aux
    return lista


def anagrama(texto1, texto2):
    texto1 = texto1.lower()
    texto2 = texto2.lower()

    lista1 = list(texto1)
    lista2 = list(texto2)

    texto1_ordenado = "".join(ordenamiento(lista1)).replace(" ", "")

    texto2_ordenado = "".join(ordenamiento(lista2)).replace(" ", "")

    return texto1_ordenado == texto2_ordenado


print(anagrama(input("Ingrese cadena1: "), input("Ingrese cadena2: ")))
