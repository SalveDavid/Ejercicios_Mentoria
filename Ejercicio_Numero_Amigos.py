# ENCONTRAR NUMEROS AMIGOS DE 1 A 1000.

def divisores(num):
    vec = []
    for i in range(1, num):
        if num % i == 0:
            vec.append(i)
    return vec


def sumatoria(vec):
    sumatoria = 0
    for i in vec:
        sumatoria = sumatoria + i
    return sumatoria


def num_amigos():

    for x in range(1, 1000):
        for y in range(1, 1000):

            vec_a = divisores(x)
            vec_b = divisores(y)

            sum_a = sumatoria(vec_a)
            sum_b = sumatoria(vec_b)

            if sum_b == x and sum_a == y:
                yield f"{x} y {y} SI son amigos"


amigo = num_amigos()

for i in amigo:
    print(i)
