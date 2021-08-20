''' Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos
para la clase:

Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.'''


class Persona():
    def __init__(self, nombre='', edad=0, DNI=''):
        self.nombre = nombre
        self.edad = edad
        self. DNI = DNI

    @property
    def name(self):
        return self.nombre

    @name.setter
    def name(self, nombre):
        self.nombre = nombre

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, edad):
        self.edad = edad

    @property
    def identification(self):
        return self.DNI

    @identification.setter
    def identification(self, DNI):
        self.DNI = DNI

    def validar_DNI(self):
        if len(self.DNI) > 8 or len(self.DNI) < 1:
            print("DNI incorrecto, debe tener entre 1 y 8 valores")
        else:
            print("DNI correcto")

    def validar_edad(self):
        if self.edad < 0:
            return print("Su edad no puede ser negativa")
        else:
            return print("Edad confirmada")

    def mostrar(self):
        return f'{self.nombre} tiene {self.edad} años y su DNI es {self.DNI}'

    def esMayorDeEdad(self):
        return True if self.edad > 18 else False


if __name__ == '__main__':
    persona1 = Persona('Pepe', -5, '19283748f')
    print(persona1.mostrar())
    print(persona1.esMayorDeEdad())
    persona1.nombre = 'Fulano'
    print(persona1.mostrar())
    persona1.validar_DNI()
    persona1.validar_edad()
