# ENCONTRAR NUMEROS PRIMOS DE 1 A 100.

# def numeros_primos():
#     # Mucha lógica aquí dentro
#     # y su yield
#
#
# for primo in numeros_primos():
#     print (primo)
#
# # => 1
# # => 2
# # => 3
# # ...

def numeros_primos():
    numero = 2
    n = 0

    yield numero

    while n <= 100:
        valor = numero + 1
        i = 1
        resto = 0

        while i <= valor:
            if valor % i == 0:
                resto += 1
            if resto > 2:
                break
            i += 1

        numero = valor

        if numero >= 101 or n >= 100:
            break

        if resto == 2:
            yield numero
    n += 1


primo = numeros_primos()

for i in primo:
    print(i)