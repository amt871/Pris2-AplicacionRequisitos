
while True:
    print('1 - Agregar cliente')
    print('2 - Agregar requisito')
    print('3 - Asignar opinion de cliente a requisito')
    print('4 - Recomendacion de un cliente a otro')
    print('5 - Crear Sprints')
    print('6 - Salir')

    opcion = int(input('Ingrese una opcion: '))

    if opcion == 1:
        nombre = input('Ingrese el nombre del cliente: ')
        id = input('Ingrese el ID del cliente: ')
        clientes.append(Cliente(nombre, id))
    elif opcion == 2:
        req = input('Ingrese el nombre del requisito: ')
        valor = int(input('Ingrese el valor del requisito: '))
        requisitos[req] = valor
    #elif opcion == 3:
     
    #elif opcion == 4:
        
    #elif opcion == 5:
       
       
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.opiniones = {}
        self.recomendaciones = set()

    def agregar_opinion(self, requisito, opinion):
        self.opiniones[requisito] = opinion

    def agregar_recomendacion(self, cliente):
        self.recomendaciones.add(cliente)

class Requisito:
    def __init__(self, nombre):
        self.nombre = nombre
        

class Sprint:
    def __init__(self, requisitos):
        self.requisitos = requisitos
        self.trabajo_realizado = set()
  
