#%% Clases
class Empleado:
    def __init__(self, id_empleado, nombre, edad):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.edad = edad

class Asalariado(Empleado):
    def __init__(self, id_empleado, nombre, edad, salario):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

class Temporal(Empleado):
    def __init__(self, id_empleado, nombre, edad, horas, dinero_hora):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.edad = edad
        self.horas = horas
        self.dinero_hora = dinero_hora

class Empresa:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.empleados = []
        self.direccion = direccion

    def agregar_empleado(self):
        id_empleado = input("Introduce el id_empleado del empleado: ")
        nombre = input("Introduce el nombre del empleado: ")
        edad = input("Introduce la edad del empleado: ")

        opcion = int(input("Seleccione el tipo:\n1-Asalariado\n2-Temporal\n"))
        if opcion == 1:
            salario = float(input("Introduce el salario del empleado: "))
            empleado = Asalariado(id_empleado, nombre, edad, salario)
        else:
            horas = int(input("Introduce las horas del empleado: "))
            dinero_hora = float(input("Introduce el dinero/hora del empleado: "))
            empleado = Temporal(id_empleado, nombre, edad, horas, dinero_hora)

        self.empleados.append(empleado)

    def calcular_salario_total(self):
        sueldos_empresa_mensual = 0
        for empleado in self.empleados:
            if isinstance(empleado, Asalariado):
                sueldos_empresa_mensual += empleado.salario
            elif isinstance(empleado, Temporal):
                sueldos_empresa_mensual += empleado.horas * empleado.dinero_hora
        return sueldos_empresa_mensual

    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(f"---------------------")
            print(f"ID: {empleado.id_empleado}, Nombre: {empleado.nombre}, Edad: {empleado.edad}")
            if isinstance(empleado, Asalariado):
                print(f"Salario: {empleado.salario}")
            elif isinstance(empleado, Temporal):
                print(f"Horas: {empleado.horas}, Dinero/Hora: {empleado.dinero_hora}")
            print(f"---------------------")

#%% Métodos
def menu_opciones():
    empresa = Empresa("Salinas", "Calle salinas 123")
    while True:
        print("Opciones de la Empresa:")
        print("1. Agregar empleados")
        print("2. Mostrar empleados")
        print("3. Calcular gasto mensual")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            empresa.agregar_empleado()
        elif opcion == 2:
            empresa.mostrar_empleados()
        elif opcion == 3:
            print(f"El gasto mensual es: {empresa.calcular_salario_total()}")
        elif opcion == 4:
            break
        else:
            print("Opción no válida, intenta de nuevo.")


menu_opciones()
        
        
        
    
        



