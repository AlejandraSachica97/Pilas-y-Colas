import Pilas
import Colas
import Interactivos

def principal():
    while True:

        print("TALLER DE PILAS Y COLAS \n")
        
        print("1. Historial \n2. Bandejas\n3. Banco\n4. Impresión")
        print("5. Menú Interactivo Pilas\n6. Menú Interactivo Colas\n0. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == "1": Pilas.Historial()
        elif opcion == "2": Pilas.Bandejas()
        elif opcion == "3": Colas.Banco()
        elif opcion == "4": Colas.Impresion()
        elif opcion == "5": Interactivos.Pilas()
        elif opcion == "6": Interactivos.Colas()
        elif opcion == "0": break
        else: print("Opción no válida.")

if __name__ == "__main__":
    principal()