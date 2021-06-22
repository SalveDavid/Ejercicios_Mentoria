# Create a class Person with te attributes:
# - name
# - lastname
# - age
# - address
#
# Functionality:
# - The attributes are mandatory to create an object from this class.
# - The name and lastname should be private.
# - Add a method to return the person's fullname.
# - Create some instances of this class as an example.
# - Add a method to this class in order to return an instance of Person without the age.
# - Add a variable to the class that allow us to know how many instances of Person has been created.
# - Create a class Employee that inherits the behaviors of Person. Include the following attributes:
#    - employee code
#    - salary per hour
#    - start date
#    - position
#    - the department what they belong
# - Add some tests to validate this functionality

class Person:

    contador = 0
    cordones = 2
    par_zapatos = 2
    ropa = 'traje'  #DUDA, NO SE PUEDE USAR CON STRING?

    def __init__(self, name, lastname, age, address):
        self.__name = name
        self.__lastname = lastname
        self.age = age
        self.address = address
        Person.contador += 1

    def fullname(self):
        return f"{self.__name} {self.__lastname} {self.zapatos(2)}"

    def without_age(self):
        return f"{self.__name} {self.__lastname} vive en {self.address}"

    @staticmethod
    def zapatos(par):
        return f"debe llevar puestos los {par} zapatos"


class Employee(Person):

    def __init__(self, name, lastname, age, address, employee_code, salary_per_hour, start_date, position, department):
        super().__init__(name, lastname, age, address)
        self.employee_code = employee_code
        self.salary_per_hour = salary_per_hour
        self.start_date = start_date
        self.position = position
        self.department = department

    def empleado_completo(self):
        return f"{self.fullname()} tiene {self.age} años, vive en {self.address}, \n" \
               f"Su código de empleado es {self.employee_code}, \n" \
               f"Su salario en de {self.salary_per_hour} dolares y empezó en la fecha {self.start_date}, \n" \
               f"Su posición es {self.position} y está en el departamento {self.department}"

    @classmethod
    def ropa(cls, bolsas):
        return f" Debe llevar sus {cls.par_zapatos} zapatos, con sus {cls.cordones} cordones y estar en {cls.ropa}" \
               f" y debe llevar {bolsas} bolsas"


persona1 = Person("Pepe", "Perez", 30, "Caracas")
persona2 = Person("Misifu", "Godinez", 40, "Rosario")
persona3 = Person("Techno", "Mantech", 35, "Miami")
persona4 = Person("Silvester", "Stallone", 75, "Los Angeles")
persona5 = Person("Keanu", "Reves", 55, "New York")
persona6 = Person("Jack", "Nicholson", 78, "Who knows")

empleado1 = Employee("Pepito", "Peruño", 40, "Barquisimeto", 101, 2500, "24-06-2021", "Programador", "IT")
empleado2 = Employee("Masafa", "Dineza", 46, "Toronto", 102, 2000, "21-07-2021", "Arquitecto", "Arquitectura")
empleado3 = Employee("Paulina", "Rubio", 53, "Cancun", 103, 3500, "12-03-2021", "Gerente", "Gerencia")

print(empleado2.ropa(5))
# print(empleado3.zapatos())
# print(empleado3.empleado_completo())
# print(persona5.without_age())
# print(Person.contador, "Instancias de Person han sido creadas")
# print(persona2.fullname())
# print(persona1.address)
# print(persona3.age)


