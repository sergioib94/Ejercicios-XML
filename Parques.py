def Listar (doc):
    lista = doc.xpath('//situacion/text()')
    return lista

def Contar (doc):
    lista = []
    nombre = doc.xpath ('//situacion/text()')
    for parques in doc.xpath ('//parques'):
        equipamientos = parques.xpath ('count(./equipamiento/equipa)')
        lista.append (int(equipamientos))
    return zip (nombre,lista)

def Filtrar (situacion,loc,doc):
    if situacion == "barrio":
        parques = doc.xpath ('//parques[barrio="%s"]/.//situacion/text()' %loc)
        return parques
    else:
        parques =doc.xpath ('//parques[pedania="%s"]/.//situacion/text()' %loc)
        return parques

def Buscar (equipo,doc):
    equipamientos = doc.xpath ('//equipamiento[equipa="%s"]/../situacion/text()' %equipo)
    return equipamientos

def localizar (parque,doc):
    latitud = doc.xpath('//parques[situacion="%s"]/./latitud/text()' %parque)
    longitud = doc.xpath('//parques[situacion="%s"]/./longitud/text()' %parque)

    mapa = "http://www.openstreetmap.org/#map=20/%s/%s"%(latitud[0],longitud[0])

    return mapa

from lxml import etree
doc = etree.parse ('parques_municipales_lorca.xml')

while True:
    print ('''Menu:
        1.Listar información: Mostrar localizacion de los distintos parques de Lorca.
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
            print (nombre,"->",total)
    elif opcion == "3":
        situacion = input("Comprobar barrio o pedania: ")
        if situacion == "barrio" or situacion == "pedania":
            localizacion = input("situacion: ")
            for localizacion in Filtrar (situacion,localizacion,doc):
                print ("*",localizacion)
        else:
            print ("Esa opcion no es valida")
    elif opcion == "4":
        equipamiento = input("equipamiento: ")
        for equipamiento in Buscar (equipamiento,doc):
            print ("*",equipamiento)
    elif opcion == "5":
        parque = input("Dime el nombre de un parque para obtener su localizacion: ")
        print (localizar(parque,doc))
    elif opcion == "0":
        break;
    else:
        print ("ERROR, esa opcion no existe")
