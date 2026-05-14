from collections import deque

def Pilas():
    pila = []
    while True:
        print("\n MENÚ INTERACTIVO PILAS")
        print("1. Agregar elemento\n2. Eliminar elemento\n3. Mostrar pila\n4. Volver")
        opc = input("Seleccione una opción: ")
        if opc == "1":
            item = input("Elemento a agregar: ")
            pila.append(item)
        elif opc == "2":
            if pila: print(f"Eliminado: {pila.pop()}")
            else: print("La pila está vacía.")
        elif opc == "3":
            print(f"Pila actual: {pila}")
        elif opc == "4":
            break

def Colas():
    cola = deque()
    while True:
        print("\n MENÚ INTERACTIVO COLAS")
        print("1. Agregar cliente\n2. Atender cliente\n3. Mostrar cola\n4. Volver")
        opc = input("Seleccione una opción: ")
        if opc == "1":
            cliente = input("Nombre del cliente: ")
            cola.append(cliente)
        elif opc == "2":
            if cola: print(f"Atendiendo a: {cola.popleft()}")
            else: print("No hay clientes en espera.")
        elif opc == "3":
            print(f"Cola actual: {list(cola)}")
        elif opc == "4":
            break