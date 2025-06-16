compras = []
def comprar_entrada():
    nombre = input("Ingrese nombre de comprador: ")
    entrada = input("Ingrese tipo de entrada (G/V): ")
    codigo = int(input("Ingrese código de confirmación:"))

    compra = {
        "nombre": nombre,
        "entrada": entrada,
        "codigo": codigo
    }
    compras.append(compra)
    print("¡Entrada registrada con éxito!")
    return

def consultar_comprador():
    if not compras:
        print("¡No existe ninguna compra registrada!")
        return
    else:
        nombre_comprador = input("Ingrese nombre de comprador a buscar: ")
        existe = False
        for compra in compras:
            if nombre_comprador == compra["nombre"]:
                existe = True
                print(f"Tipo de entrada: {compra["entrada"]}, Código: {compra["codigo"]}")
                return
        if not existe:
            print("El comprador no se encuentra.")

def cancelar_compra():
    if not compras:
        print("¡No existe ninguna compra registrada!")
        return
    else:
        nombre_comprador = input("Ingrese nombre de comprador a buscar: ")
        existe = False
        for compra in compras:
            if nombre_comprador == compra["nombre"]:
                existe = True
                compras.remove(compra)
                print("¡Compra cancelada!")
                return
        if not existe:
            print("No se pudo cancelar la compra.")