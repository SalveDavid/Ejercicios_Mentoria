# Write a decorator to validate te function's input to make sure that all the parameters are the
# types that you specified beforehand

# For example:
# @check_types(int,float,str)
# def f(a,b,c)


def Tipos_de_datos(*tipos_de_datos):
    # for _ in tipos_de_datos:
    #     print(_)

    def wrapp1(datos_a_comparar):

        def wrapp2(*datos_a_b_c):

            for i in range(len(datos_a_b_c)):
                if type(datos_a_b_c[i]) == tipos_de_datos[i]:
                    print(True)
                else:
                    print(False)

        return wrapp2

    return wrapp1


@Tipos_de_datos(int, float, str)
def datos_a_comparar(a, b, c):
    pass


datos_a_comparar(1, 2.5, "hola")