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
        parques = doc.xpath ('//parques[pedania="%s"]/.//situacion/text()' %loc)
        return parques

def Buscar (equipo,doc):
    equipamientos = doc.xpath ('//equipamiento[equipa="%s"]/../situacion/text()' %equipo)
    return equipamientos

def Localizar (parque,doc):
    latitud = doc.xpath('//parques[situacion="%s"]/./latitud/text()' %parque)
    longitud = doc.xpath('//parques[situacion="%s"]/./longitud/text()' %parque)

    mapa = "http://www.openstreetmap.org/#map=20/%s/%s"%(latitud[0],longitud[0])

    return mapa

def Ayuda (opcion,doc):
    if opcion == "1":
        lista = doc.xpath ('//barrio/text()')
        return lista
    elif opcion == "2":
        lista2 = doc.xpath ('//pedania/text()')
        return lista2
    elif opcion == "3":
        lista3 = doc.xpath ('//equipamiento/equipa/text()')
        return lista3
    else:
        print ("La opcion no existe")

from lxml import etree
doc = etree.parse ('parques_municipales_lorca.xml')

while True:
    print ('''Menu:
        1.Listar información: Mostrar localizacion de los distintos parques de Lorca.
        2.Contar información: Mostrar la cantidad de equipamientos con la que cuenta cada parque.
        3.Buscar o filtrar información: Pedir por teclado una localizacion y mostrar si hay mas de un parque en esa localización.
        4.Buscar informacion relacionada: Pedir por teclado un equipamiento y mostrar los parques que cuenten con ese equipamiento.
        5.Ejercicio libre: Buscar la situacion de un parque dado por teclado y mostrarlo en un mapa openstreetmap usando la longitud y la latitud.
        6.Ayuda XML.
        0.Salir''')

    opcion = input("opcion: ")

    if opcion == "1":
        for parques in Listar (doc):
            print ("*",parques)

    elif opcion == "2":
        for nombre ,total in Contar (doc):
            print (nombre,"->",total)

    elif opcion == "3":
        situacion = input("Comprobar barrio o pedania: ")
        if situacion == "barrio" or situacion == "pedania":
            loc = (input("situacion (debe ponerse en mayusculas): "))
            for loc in Filtrar (situacion,loc,doc):
                print ("*",loc)
        else:
            print ("Esa opcion no es valida")

    elif opcion == "4":
        equipamiento = input("equipamiento: ")
        for equipamiento in Buscar (equipamiento,doc):
            print ("*",equipamiento)

    elif opcion == "5":
        parque = input("Dime el nombre de un parque para obtener su localizacion: ")
        print (Localizar(parque,doc))

    elif opcion == "6":
        print ('''Menu de Ayuda:
            1.Lista de Barrios
            2.Lista de Pedanias
            3.Lista de Equipamientos''')

        opcion = input("opcion: ")

        if opcion == "1":
            for barrios in Ayuda (opcion,doc):
                print ("*",barrios)

        if opcion == "2":
            for pedania in Ayuda (opcion,doc):
                print ("*",pedania)

        if opcion == "3":
            for equipamiento in Ayuda (opcion,doc):
                print ("*",equipamiento)

    elif opcion == "0":
        break;

    else:
        print ("ERROR, esa opcion no existe")
