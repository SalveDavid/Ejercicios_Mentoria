#  Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad
# (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos
# para la clase:

# Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando
# o retirando dinero.
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Cuenta:
    def __init__(self, titular='', cantidad=0):
        self. titular = titular
        self.cantidad = cantidad

    @property
    def cliente(self):
        return self.titular

    @cliente.setter
    def cliente(self, titular):
        self.titular = titular

    @property
    def money(self):
        return self.cantidad

    @money.setter
    def money(self, cantidad):
        self.cantidad = cantidad

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            return self.cantidad

    def retirar(self, retiro):
        self.cantidad -= retiro
        return self.cantidad

    def mostrar(self):
        return f'{self.titular} tiene {self.cantidad} US$'


if __name__ == '__main__':
    titular1 = Cuenta('Jose', 10000)
    print(titular1.mostrar())
    print(titular1.ingresar(50))
    print(titular1.retirar(257))
    print(titular1.mostrar())
    print(titular1.retirar(12000))
    print(titular1.mostrar())



