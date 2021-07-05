# Write a function to read a file with employees details.

# This is a file separated by ";", named empleados.txt which contains the names of the columns in the first line
# like this:
# - employee_code
# - name
# - lastname
# - address
# - age
# - start_date
# - salary
# - position
# - department

# This file could contain repeated records. You'll need to think of a way to get unique employees or unique records.

# Functionality:
# - Get the employees with the lower rate per hour (lower salary). You can see comprehensions to solve it.
# - Add some tests to validate this functionality

matriz_con_coma = []
matriz_con_coma_sin_primeracolumna = []
matriz_con_coma_sin_repeticiones = []
diccionario = {}
lista2 = []
menor = None
mayor = None

with open('empleados.txt') as file:
    lista_con_punto_y_coma = [con_punto_y_coma.rstrip() for con_punto_y_coma in file]   # convierto el archivo en lista de strings
    for con_punto_y_coma in lista_con_punto_y_coma:
        matriz_con_coma.append(con_punto_y_coma.split(";"))  # Cambio acá los ";" a ",", convirtiendo la lista en matriz

for colum in matriz_con_coma:
    del colum[0]
    matriz_con_coma_sin_primeracolumna = matriz_con_coma  # Borro la primera columna de la matriz

for i in matriz_con_coma_sin_primeracolumna:
    if i not in matriz_con_coma_sin_repeticiones:
        matriz_con_coma_sin_repeticiones.append(i)  # Borro las filas repetidas de la matriz

for fila in range(1, len(matriz_con_coma_sin_repeticiones)):  # Voy cambiando la matriz a diccionario con los valores que me interesan
    columna = 5
    llave = matriz_con_coma_sin_repeticiones[fila][columna]
    valor = matriz_con_coma_sin_repeticiones[fila][columna - 5]
    valor2 = matriz_con_coma_sin_repeticiones[fila][columna - 4]
    diccionario[llave] = f"{valor} {valor2}"

lista = list(diccionario)  # Convierto el dicionario a una lista de strings

for i in range(len(lista)):
    lista2.append(int(lista[i]))   # Cambio la lista de strings por lista de enteros

for num in lista2:
    if menor == None and mayor == None:
        menor = num
        mayor = num
    else:
        if num < menor:
            menor = num
        elif num > mayor:
            mayor = num

menor = str(menor)
mayor = str(mayor)

print(f"The employee with lower salary is: {diccionario[menor]} with US${menor}")
print(f"The employee with higher salary is: {diccionario[mayor]} with US${mayor}")











