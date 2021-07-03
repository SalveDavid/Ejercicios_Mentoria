# Write a decorator to validate te function's input to make sure that all the parameters are the
# types that you specified beforehand

# For example:
# @check_types(int,float,str)
# def f(a,b,c)


def Tipos_de_datos(*tipos_de_datos):

    def wrapp1(datos_a_comparar):

        def wrapp2(*datos_a_b_c_d):

            for i in range(len(datos_a_b_c_d)):
                # try:
                    if type(datos_a_b_c_d[i]) == tipos_de_datos[i]:
                        print(True)
                    else:
                        raise Exception("La variable no corresponde")
                # except Exception as error:
                #     raise Exception(error)

        return wrapp2

    return wrapp1


@Tipos_de_datos(int, float, str, bool)
def datos_a_comparar(a, b, c, d):
    pass


datos_a_comparar(True, 2.5, 4, False)
