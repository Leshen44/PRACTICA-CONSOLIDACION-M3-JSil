nombres = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes",
]
magos = []
cientificos = []
otros = []
for i in nombres:
    if i == "Harry Houdini" or i == "David Blaine" or i == "Teller":
        magos.append(i)
    elif i == "Newton" or i == "Hawking" or i == "Einstein":
        cientificos.append(i)
    else:
        otros.append(i)

def hacer_grandioso(magos):
    lista=[]
    for i in magos:
        i = "El gran " + i
        lista.append(i)
    return lista

def imprimir_nombres(mensaje, lista):
    print(f"----{mensaje}---")
    for i in lista:
        print(i)

magos_grandiosos = hacer_grandioso(magos)
imprimir_nombres("Lista completa", nombres)
imprimir_nombres("Magos grandiosos", magos_grandiosos)
imprimir_nombres("Cientificos", cientificos)
imprimir_nombres("Otros", otros)
