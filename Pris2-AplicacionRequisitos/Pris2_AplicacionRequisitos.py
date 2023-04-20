class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.importancia = 1

    def agregar_recomendacion(self):
        self.importancia = self.importancia +  1
        print('El valor actual del Cliente es ' + str(self.importancia))


class Requisito:
    def __init__(self, nombre):
        self.nombre = nombre
        self.valor = 1

    def agregar_valor(self, cliente):
        self.valor = self.valor + cliente.importancia
        print('El valor actual del Requisito es ' + str(self.valor))
        

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
        input('Presione enter para continuar...')
    elif opcion == 2:
        req = input('Ingrese el nombre del requisito: ')
        requisitos.append(Requisito(req))
        input('Presione enter para continuar...')
    elif opcion == 3:
        for i in range(len(clientes)):
            print(i, clientes[i].nombre)
        persona = int(input('Ingrese el numero del persona: '))
        for i in range(len(requisitos)):
            print(i, requisitos[i].nombre)
        req = int(input('Ingrese el numero del requisito: '))
        requisitos[req].agregar_valor(clientes[persona])
        input('Presione enter para continuar...')
    
     
    elif opcion == 4:
        for i in range(len(clientes)):
            print(i, clientes[i].nombre)
        persona = int(input('Ingrese el numero del persona: '))
        clientes[persona].agregar_recomendacion() 
        input('Presione enter para continuar...')

         
    #elif opcion == 5:
       
    elif opcion == 6:
       sys.exit(0)
