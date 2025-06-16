#Resources
compras = []
#Resources
#Functions
def comprar_entrada():
    nombre = validar_nombre()
    entrada = validar_tipo_entrada()
    codigo = validar_codigo()

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
        for compra in range(len(compras)):
            if nombre_comprador == compra["nombre"]:
                existe = True
                compras.pop(compra)
                print("¡Compra cancelada!")
                return
        if not existe:
            print("No se pudo cancelar la compra.")
#Functions

#Validations
def validar_nombre():
    while True:
        try:
            nombre = input("Ingrese nombre del comprador: ").strip()
            existe = False
            if compras:
                for compra in compras:
                    if nombre == compra["nombre"]:
                        existe = True
                        print("¡Nombre de comprador ya existe!")
                        break
            if not existe:
                return nombre
        except:
            print("Error. Dato ingresado inválido.")

def validar_tipo_entrada():
    while True:
        try:
            entrada = input("Ingrese tipo de entrada (G/V): ")
            if entrada == "G" or entrada == "V":
                return entrada
            else:
                print("Solo se permite ingresar la letra “G” (General) y “V” (VIP).")
        except:
            print("Error. Dato ingresado inválido.")

def validar_codigo():
    while True:
        try:
            codigo = input("Ingrese código de confirmación: ").strip()
            if len(codigo) >= 6:
                return codigo
            else:
                print("Error. Código inválido, debe tener mínimo 6 caracteres, 1 letra mayúscula, 1 número y sin espacios en blanco.")
        except:
            print("Error. Dato ingresado inválido.")
#Validations