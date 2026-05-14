from collections import deque

def Banco():
    print("\n Turnos del Banco ")
    cola_banco = deque()
    clientes = "Ana", "Alejandra", "Luisa", "Pedro"
    for c in clientes:
        cola_banco.append(c)
    
    print(f"Fila actual: {list(cola_banco)}")
    print(f"Atendiendo: {cola_banco.popleft()}")
    print(f"Atendiendo: {cola_banco.popleft()}")
    print(f"Siguiente cliente: {cola_banco[0]}")

def Impresion():
    print("\n Impresión pendientes")
    cola_docs = deque("Doc1.pdf", "Foto.jpg", "Taller.docx", "Nota.txt", "Planilla.xlsx")
    print(f"Cola de impresión: {list(cola_docs)}")
    
    for _ in range(3):
        print(f"Imprimiendo: {cola_docs.popleft()}")
    
    print(f"Documentos pendientes: {list(cola_docs)}")