def Historial():
    print("\n Historial del Navegador ")
    pila_historial = []
    paginas = "Google", "YouTube", "Classroom", "GitHub"
    for p in paginas:
        pila_historial.append(p)
    
    print(f"Historial: {pila_historial}")
    print(f"Se cerró: {pila_historial.pop()}")
    print(f"Se cerró: {pila_historial.pop()}")
    print(f"Página actual: {pila_historial[-1]}")

def Bandejas():
    print("\n Pila de Bandejas")
    bandejas = []
    colores = "Rosada", "Morada", "Gris", "Roja", "Cafe"
    for c in colores:
        bandejas.append(c)
    
    print(f"Pila inicial: {bandejas}")
    bandejas.pop()
    bandejas.pop()
    print(f"Pila final: {bandejas}")