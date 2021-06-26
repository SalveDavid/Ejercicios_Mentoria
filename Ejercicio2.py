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
k = 1
menor = 0
sueldos = []
sueldos2 = []

with open('empleados.txt') as file:
    lista_con_punto_y_coma = [con_punto_y_coma.rstrip() for con_punto_y_coma in file]
#print(lista_con_punto_y_coma)

for con_punto_y_coma in lista_con_punto_y_coma:
    lista_de_listas_con_coma.append(con_punto_y_coma.split(";"))
#print(lista_de_listas_con_coma)

for i in range(1, len(lista_de_listas_con_coma)):
    lista_de_listas_con_coma_sin_primeralinea.append(lista_de_listas_con_coma[i])
#print(lista_de_listas_con_coma_sin_primeralinea)

for colum in lista_de_listas_con_coma_sin_primeralinea:
    del colum[0]
    lista_de_listas_con_coma_sin_primeracolumna = lista_de_listas_con_coma_sin_primeralinea
#print(lista_de_listas_con_coma_sin_primeracolumna)


for i in lista_de_listas_con_coma_sin_primeracolumna:
    if i not in lista_de_listas_con_coma_sin_repeticiones:
        lista_de_listas_con_coma_sin_repeticiones.append(i)
print(lista_de_listas_con_coma_sin_repeticiones)


# for i in range(len(lista_de_listas_con_coma_sin_repeticiones)):
#     for j in range(5, 6):
#         sueldos.append(lista_de_listas_con_coma_sin_repeticiones[i][j])

sueldos2 = [sueldos.append(lista_de_listas_con_coma_sin_repeticiones[i][j]) for j in range(5, 6) for i in
            range(len(lista_de_listas_con_coma_sin_repeticiones))]
print(sueldos)

for i in range(len(sueldos)-1):
    if sueldos[i] < sueldos[i + 1]:
        menor = sueldos[i]
        sueldos[i] = sueldos[i + 1]
        sueldos[i + 1] = menor
print("El menor sueldo es: ", menor)











