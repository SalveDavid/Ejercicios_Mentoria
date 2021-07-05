# ENCONTRAR NUMEROS PRIMOS DE 1 A 100.

for n in range(1, 101):
    cant_divisores = 0
    i = 1
    while i <= n:
        if n % i == 0:
            cant_divisores += 1
        i += 1
    if cant_divisores == 2:
        print(f"El número {n} es primo")
    else:
        print(f"El número {n} NO es primo")

