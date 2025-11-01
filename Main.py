import os.path
from Clase import *

#Validar un rango dentro de un minimo y un maximo
def validar_rango(inf, sup, msj):
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor

#Carga un archivo de texto que contiene las direcciones y las transforma en un objeto de la clase envio,
# definidos en Clase.py, y los agrega a un vector que contiene todos estos objetos
def cargar_desde_archivo(v, tc, FD):
    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe...')
        print('Revise..')
        return

    pr = True
    m = open(FD, "rt")
    for line in m:
        if pr is True:
            if "SC" in line:
                tc = "SC"
            pr = False

        else:
            cp = line[0:9].strip().upper()
            direccion = line[9:29].strip()
            tipo = int(line[29])
            pago = int(line[30])

            env = Envio(cp, direccion, tipo, pago)
            v.append(env)

    m.close()
    return tc
#Busca un envio por su direccion y su tipo, si no lo encuentra, retorna -1
def buscar_envio_direccion_tipo(v, d, e):
    for envios in v:
        if d == envios.direccion and e == envios.tipo:
            return envios
    return -1

#Devuelve true si la direccion no contiene caracteres especiales, no hay dos mayusculas seguidas
# y si cada palabra contiene la misma cantidad de letras y digitos
def validar_envio(direccion):
    cl = cd = 0
    td = False
    ant = " "
    for car in direccion:
        if car in " .":
            if cl == cd:
                td = True
            cl = cd = 0
            ant = " "

        else:
            cl += 1
            if not car.isdigit() and not car.isalpha():
                return False
            if ant.isupper() and car.isupper():
                return False
            if car.isdigit():
                cd += 1
            ant = car
    return td

#Calcula el importe final de un envio por su region (primer digito del codigo postal), pais, tipo de envio y su forma de pago
def importe_final(cp, pais, tipo, fp):
    precios = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    monto = precios[tipo]

    if pais == "Argentina":
        inicial = monto
    else:
        if pais == "Bolivia" or pais == "Paraguay":
            inicial = int(monto * 1.20)
        elif pais == "Uruguay":
            if cp[0] == 1:
                inicial = int(monto * 1.20)
            else:
                inicial = int(monto * 1.25)
        elif pais == "Chile":
            inicial = int(monto * 1.25)
        elif pais == "Brasil":
            if cp[0] == '8' or cp[0] == '9':
                inicial = int(monto * 1.20)
            else:
                if cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3':
                    inicial = int(monto * 1.25)
                else:
                    inicial = int(monto * 1.30)
        else:
            inicial = int(monto * 1.50)
    final = inicial
    if fp == 1:
        final = int(0.9 * inicial)
    return final



#Crea un vector vacio y la carga con todos los objetos utilizando cargar_desde_archivo,
# si ya estan cargados, da la opcion de borrar los datos previos
def opcion1(v, tc, fd):
    if len(v) != 0:
        r = int(input("¿Desea borrar los datos previos? (1: Si - 2: No (volver al menu): "))
        if r == 1:
            v = []
            tc = cargar_desde_archivo(v, tc, fd)
            print("Carga terminada...")
    else:
        tc = cargar_desde_archivo(v, tc, fd)
        print("Carga terminada...")

    print()
    return v, tc

#Crea un vector vacio y lo llena con objetos de la clase envio cargados por teclado
def opcion2(v):
    m = validar_rango(1, 5, "Cuantos registros quiere agregar al arreglo (al menos 1 y no mas de 5)?: ")

    for i in range(m):
        cod = input("Codigo postal: ")
        dp = input("Direccion postal: ")
        tip = validar_rango(0, 6, "Tipo de envio (entre 0 y 6): ")
        fp = validar_rango(1, 2, "Forma de pago (entre 1 y 2): ")

        env = Envio(cod, dp, tip, fp)
        v.append(env)

    print("Carga terminada")
    print()

#Ordenamiento secuencial por el codigo de los objetos un vector
def ordenar(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]

#Muestra una cantidad de registros indicada por teclado
def opcion3(v):
    n = len(v)
    ordenar(v)
    print("Hay", n, "registros en el arreglo")
    m = validar_rango(1, n, "Cantidad a mostrar (al menos 1 y no mas de " + str(n) + ")?: ")
    print("Listado de envios ordenados por codigo postal...")
    for i in range(m):
        print(v[i])

    print()

#Busca un objeto en especifico por su direccion y por su tipo en el vector utilizando la funcion buscar_envio_direccion_tipo
def opcion4(v):
    d = (input("Ingrese direccion de envio a encontrar(con un . al final):"))
    e = int(input("Ingrese el tipo del envio solicitado: "))
    return buscar_envio_direccion_tipo(v, d, e)

#Esta opcion busca un objeto por codigo postal
def opcion5(v):
    cp = input("Ingrese codigo postal: ")
    for envios in v:
        if cp == envios.codigo:
            if envios.pago == 1:
                tipoanterior = 1
                envios.pago = 2
            else:
                tipoanterior = 2
                envios.pago = 1
            return envios, tipoanterior
    return -1, -1

#Muestra los envios de cada tipo en un vector contador
def opcion6_SC(v):
    vc = [0] * 7
    for envios in v:
        vc[envios.tipo] += 1
    for i in range(len(vc)):
        print("Cantidad de envios del tipo", i, ": ", vc[i])

#Muestra los envios validos de cada tipo en un vector contador
def opcion6_HC(v):
    vc = [0] * 7
    envios_validos = 0
    for envios in v:
        if validar_envio(envios.direccion):
            vc[envios.tipo] += 1
            envios_validos += 1
    print("Cantidad de envios validos: ", envios_validos)
    for i in range(len(vc)):
        print("Cantidad de envios del tipo ", i,": ", vc[i])

#Muestra la sumatoria de los importes de los envios validos por tipo
def opcion7_HC(v):
    va = [0] * 7
    for envios in v:
        if validar_envio(envios.direccion):
            va[envios.tipo] += importe_final(envios.codigo, envios.country(), envios.tipo, envios.pago)
    for i in range(len(va)):
        print("Acumulacion de importes finales de los envios del tipo", i,": ", va[i])
    return va

#Muestra la sumatoria de los envios por tipo
def opcion7_SC(v):
    va = [0] * 7
    for envios in v:
        va[envios.tipo] += importe_final(envios.codigo, envios.country(), envios.tipo, envios.pago)
    for i in range(len(va)):
        print("Acumulacion de importes finales de los envios del tipo", i,": ", va[i])
    return va

#Muestra el tipo con mayor acumulacion de importes, y el porcentaje que representa respecto de la totalidad de importes
def opcion8(va):
    importemayor = 0
    acum1 = 0
    for i in range(len(va)):
        importe = va[i]
        if importe > importemayor:
            importemayor = importe
            tipoim = i
    for montos in va:
        acum1 += montos
    if acum1 != 0:
        porc = int((importemayor * 100) / acum1)
        print("El tipo de envio con mayor acumulacion de importes es el:", tipoim, "Y representa un", porc,"%","de la totalidad de importes")
    else:
        print("No hay importes cargados, porfavor ingresar envios para poder hacer los calculos")

#Muestra el promedio de todos los importes finales de los envios, y la cantidad de envios con importes menores
# al promedio
def opcion9(v):
    acum1 = cont1 = cont2 = 0
    for envios in v:
        acum1 += importe_final(envios.codigo, envios.country(), envios.tipo, envios.pago)
        cont1 += 1
    if cont1 != 0:
        prom = int(acum1 / cont1)
        for envios in v:
            if importe_final(envios.codigo, envios.country(), envios.tipo, envios.pago) < prom:
                cont2 += 1
        print("El promedio de todos los importes finales de los envios es:", prom)
        print("La cantidad de envios con importes finales menores al promedio es de:", cont2)
    else:
        print("No hay importes cargados, porfavor ingresar envios para poder hacer los calculos")


#Esta funcion define los parametros como el file directory (Que en este caso se encuentra en la misma carpeta
# que el script). Y define un menu de opciones que ejecuta las distintas instancias de lectura de datos que pedia la consigna
# del trabajo

def principal():
    fd = "envios-tp3.txt"

    tc = "HC"

    v = []

    va = []

    op = 0
    while op != 10:
        print("Trabajo Practico 3")
        print("1. Cargar arreglo desde archivo de texto")
        print("2. Cargar arreglo desde teclado")
        print("3. Listado ordenado")
        print("4. Busqueda por direccion")
        print("5. Busqueda por codigo postal")
        print("6. Cantidad de envios con direccion válida")
        print("7. Importe final acumulado")
        print("8. Envio con mayor importe")
        print("9. Importe final promedio")
        print("10. Salir")
        op = int(input("Ingrese numero de opcion: "))
        print("-" * 75)

        if op == 1:
            v, tc = opcion1(v, tc, fd)

        elif op == 2:
            opcion2(v)

        elif op == 3:
            if len(v) != 0:
                opcion3(v)
            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print("-" * 75)

        elif op == 4:
            x = opcion4(v)
            if x == -1:
                print("Envio no encontrado, porfavor revise si fue ingresado correctamente...")
            else:
                print("Envio encontrado! Sus datos son: ")
                print("Direccion:", x.direccion)
                print("Codigo:", x.codigo)
                print("Tipo:", x.tipo)
                print("Pais:", x.country())
                print("Forma de pago:", x.pago)
            print("-" * 75)

        elif op == 5:
            envio, tipoanterior = opcion5(v)
            if envio == tipoanterior == -1:
                print("Codigo Postal no encontrado. Verificar si fue ingresado correctamente...")
            else:
                print("Codigo encontrado!:", envio.codigo, envio.direccion)
                print("Cambio de forma de pago exitosa")
                print("Forma de pago anterior:", tipoanterior)
                print("Nueva forma de pago: ", envio.pago)

            print("-" * 75)

        elif op == 6:
            print("Tipo de Control: ", tc)
            if tc == "HC":
                opcion6_HC(v)
            elif tc == "SC":
                opcion6_SC(v)
            print("-" * 75)

        elif op == 7:
            if tc == "HC":
                va = opcion7_HC(v)
            elif tc == "SC":
                va = opcion7_SC(v)
            print("-" * 75)

        elif op == 8:
            if len(va) == 0:
                print("Para acceder a esta opcion, porfavor primero calcular los importes con la opcion 7")
            else:
                opcion8(va)
            print("-" * 75)

        elif op == 9:
            opcion9(v)
            print("-" * 75)


if __name__ == "__main__":
    principal()
