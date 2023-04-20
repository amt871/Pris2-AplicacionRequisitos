import sys
from typing import Self

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
Continuar = input('Presione enter para continuar...')
while True:
    print('1 - Agregar cliente')
    print('2 - Agregar requisito')
    print('3 - Asignar opinion de cliente a requisito')
    print('4 - Recomendacion de un cliente a otro')
    print('5 - Crear Sprints')
    print('6 - Salir')

    try:
        opcion = int(input('Ingrese una opcion: '))
    except ValueError:
        opcion = 100;
        print("El valor ingresado no es un número entero válido.")
        Continuar
    if opcion == 1:
        nombre = input('Ingrese el nombre del cliente: ')
        clientes.append(Cliente(nombre))
        
    elif opcion == 2:
        req = input('Ingrese el nombre del requisito: ')
        requisitos.append(Requisito(req))
        Continuar
    elif opcion == 3:
        for i in range(len(clientes)):
            print(i, clientes[i].nombre)
        persona = int(input('Ingrese el numero del persona: '))
        for i in range(len(requisitos)):
            print(i, requisitos[i].nombre)
        req = int(input('Ingrese el numero del requisito: '))
        requisitos[req].agregar_valor(clientes[persona])
        Continuar
    elif opcion == 4:
        for i in range(len(clientes)):
            print(i, clientes[i].nombre)
        persona = int(input('Ingrese el numero del persona: '))
        clientes[persona].agregar_recomendacion() 
        Continuar  
    elif opcion == 5:
        acabado = False
        # Ordenar requisitos por valor
        requisitos_ordenados = sorted(requisitos, key=lambda x: x.valor, reverse= True)

        # Imprimir requisitos ordenados
        esfuerzo = int(input('Ingrese el esfuerzo maximo'))
        Sprint = 1
        espacio = esfuerzo
        while acabado == False:
            print("Sprint " + str(Sprint))
            while espacio > 0:
                if len(requisitos_ordenados) == 0:
                    acabado = True
                    break
                Actual = requisitos_ordenados.pop(0)
                print(Actual.nombre)
                espacio = espacio - 1
            Sprint = Sprint + 1
            espacio = esfuerzo
        Continuar
                  
    elif opcion == 6:
       sys.exit(0)

    else :
        print('Opcion invalida')
