#   Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuentaJoven que deriva de la
# anterior. Cuando se crea esta nueva clase, además del titular y la cantidad, se debe guardar una bonificación que
# estará expresada en tanto por ciento. Construye los siguientes métodos para la clase:

#   Un constructor.
#   Los setters y getters para el nuevo atributo.
#   En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un
# método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso
# contrario.
#   Además la retirada de dinero sólo se podrá hacer si el titular es válido.
#   El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
#   Piensa los métodos heredados de la clase madre que hay que reescribir.

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


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0, edad=0):
        # super(CuentaJoven, self).__init__()
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
        self.edad = edad
        
    @property
    def bono(self):
        return self.bonificacion
    
    @bono.setter
    def bono(self, bonificacion):
        self.bonificacion = bonificacion

    def esTitularValido(self):
        return True if 18 < self.edad < 25 else False

    def retirar(self, retiro):
        if self.esTitularValido():
            super().retirar(retiro)
        else:
            print("No puede retirar,no es un usuario valido")

    def mostrar(self):
        print(f"{self.titular} tiene una bonificación de {self.bonificacion}, su cuenta ahora es de {self.bonificacion + self.cantidad}")


if __name__ == '__main__':
    titular1 = Cuenta('Pedro', 5000)
    titular2 = CuentaJoven('Susan', 6000, 50, 24)
    print("La cuenta de la persona es válida?", titular2.esTitularValido(), "\n")
    titular2.retirar(1000)
    print(f"Su saldo después del retiro es: {titular2.cantidad}")
    titular2.bonificacion = 99999
    titular2.mostrar()


