# Encontrar si una cadena de texto es palindromo.
# Consideraciones: puede ser palabra, oracion.
# Crear funcion, solo utiliza 1 cadena de texto


def palindromo(texto):

    texto = texto.lower()

    return texto == texto[::-1]


print(palindromo(input("Ingrese palabra u oración: ").replace(" ", "")))






