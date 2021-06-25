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
lista_de_listas_con_coma_sin_repeticiones = []


with open('empleados.txt') as file:
    lista_con_punto_y_coma = [con_punto_y_coma.rstrip() for con_punto_y_coma in file]
#print(lista_con_punto_y_coma)

for con_punto_y_coma in lista_con_punto_y_coma:
    #print(con_punto_y_coma)
    lista_de_listas_con_coma.append(con_punto_y_coma.split(";"))
print(lista_de_listas_con_coma)

for i in range(1, len(lista_de_listas_con_coma)):
    lista_de_listas_con_coma_sin_primeralinea.append(lista_de_listas_con_coma[i])
print(lista_de_listas_con_coma_sin_primeralinea)






