def Listar (doc):
    lista = doc.xpath('//situacion/text()')
    return lista

def Contar (doc):
    lista = []
    nombre = doc.xpath ('//situacion/text()')
    for parques in doc.xpath ('//parques'):
        equipamientos = parques.xpath ('count(//parques/equipamiento)')
        lista.append (int(equipamientos))
    return zip (nombre,lista)

from lxml import etree
doc = etree.parse ('parques_municipales_lorca.xml')

while True:
    print ('''1.Listar información: Mostrar la localizacion de los distintos parques de Lorca.
              2.Contar información: Mostrar la cantidad de equipamientos con la que cuenta cada parque.
              3.Buscar o filtrar información: Pedir por teclado una localizacion y mostrar si hay mas de un parque en esa localización.
              4.Buscar informacion relacionada: Pedir por teclado un equipamiento y mostrar los parques que cuenten con ese equipamiento.
              5.Ejercicio libre: Buscar la situacion de un parque dado por teclado y mostrarlo en un mapa openstreetmap usando la longitud y la latitud.
              0.Salir''')

    opcion = input("opcion: ")

    if opcion == "1":
        for parques in Listar (doc):
            print (parques)
    elif opcion == "2":
        for nombre ,total in Contar (doc):
            print (nombre,total)
    else:
        break
