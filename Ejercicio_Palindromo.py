# Encontrar si una cadena de texto es palindromo.
# Consideraciones: puede ser palabra, oracion.
# Crear funcion, solo utiliza 1 cadena de texto


def palindromo(texto):

    string1 = ''
    string2 = ''

    texto = texto.lower()

    for i in range(len(texto)):
        if texto[i] == ' ':
            pass
        else:
            string1 += texto[i]

    for i in range(len(string1) - 1, -1, -1):
        string2 += string1[i]

    return string1 == string2

print(palindromo(input("Ingrese palabra u oración: ")))






