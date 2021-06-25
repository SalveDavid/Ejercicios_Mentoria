'''
# Hacer un programa que, dado un valor de N dado en la consola,
# imprima las figuras como se muestra a continuación

# Valor de n:
# 5
# La primera figura es:
# *****
# *****
# *****
# *****
# *****
# <PAUSA>
# La segunda figura es:
# *
# **
# ***
# ****
# *****
# <PAUSA>
# La tercera figura es:
# *****
# ****
# ***
# **
# *
# <PAUSA>
# La cuarta figura es:
#     *
#    ***
#   *****
#  *******
# *********
'''


N = int(input("Ingrese en numero N: "))

print("La primera figura es:")
for i in range(N):
    print("*"*N)
print("<PAUSA>")

print("La segunda figura es:")
for i in range(1, N+1):
    print("*"*i)
print("<PAUSA>")

print("La tercera figura es:")
for i in range(N, 0, -1):
    print("*"*i)
print("<PAUSA>")

print("La cuarta figura es:")
for i in range(0, N):
    print(' ' * (N - i - 1) + "*" * (2 * i + 1))
print("<PAUSA>")

print("La quinta figura es:")
for i in range(N-1, -1, -1):
    print(' ' * (N - i - 1) + "*" * (2 * i + 1))
