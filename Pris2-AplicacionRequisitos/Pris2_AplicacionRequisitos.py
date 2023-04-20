class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.recomendaciones = 1

    def agregar_recomendacion(self):
        self.recomendaciones = self.recomendaciones +  1
        print('El valor actual del Cliente es' + self.recomendaciones)

class Requisito:
    def __init__(self, nombre):
        self.nombre = nombre
        self.opiniones = set()
        

class Sprint:
    def __init__(self, nombre):
        self.nombre = nombre
        
  


clientes = []
requisitos = []
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
        clientes.append(Cliente(nombre))
    elif opcion == 2:
        req = input('Ingrese el nombre del requisito: ')
        requisitos.append(Requisito(req))

    elif opcion == 3:
        for i in range(len(clientes)):
            print(i, clientes[i].nombre)
        persona = int(input('Ingrese el numero del persona: '))
        clientes[persona].agregar_recomendacion()
     
    elif opcion == 4:
        print('Hola ')
        


        
    #elif opcion == 5:
       
       
