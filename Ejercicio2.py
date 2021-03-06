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

lista_de_listas_con_coma = []
lista_de_listas_con_coma_sin_primeralinea = []
lista_de_listas_con_coma_sin_primeracolumna = []
lista_de_listas_con_coma_sin_repeticiones = []
menor = None
mayor = None
sueldos = []
sueldos2 = []

with open('empleados.txt') as file:
    lista_con_punto_y_coma = [con_punto_y_coma.rstrip() for con_punto_y_coma in file]

for con_punto_y_coma in lista_con_punto_y_coma:
    lista_de_listas_con_coma.append(con_punto_y_coma.split(";"))
print(lista_de_listas_con_coma)

for i in range(1, len(lista_de_listas_con_coma)):
    lista_de_listas_con_coma_sin_primeralinea.append(lista_de_listas_con_coma[i])

for colum in lista_de_listas_con_coma_sin_primeralinea:
    del colum[0]
    lista_de_listas_con_coma_sin_primeracolumna = lista_de_listas_con_coma_sin_primeralinea

for i in lista_de_listas_con_coma_sin_primeracolumna:
    if i not in lista_de_listas_con_coma_sin_repeticiones:
        lista_de_listas_con_coma_sin_repeticiones.append(i)


sueldos2 = [sueldos.append(lista_de_listas_con_coma_sin_repeticiones[i][j]) for j in range(5, 6) for i in
            range(len(lista_de_listas_con_coma_sin_repeticiones))]

for num in sueldos:
    if menor == None and mayor == None:
        menor = num
        mayor = num
    else:
        if num < menor:
            menor = num
        elif num > mayor:
            mayor = num


print("El menor sueldo es: ", menor)












