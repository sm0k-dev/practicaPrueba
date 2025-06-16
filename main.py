#Libraries
import os, time, msvcrt
#Libraries
#MenuText
menu = """MENU PRINCIPAL
1.- Comprar entrada.
2.- Consultar comprador.
3.- Cancelar compra.
4.- Salir.
"""
#MenuText
#Menu
while True:
    os.system('cls')
    print(menu)
    option = input("Ingrese opción (1-4): ")
    os.system('cls')
    #Options
    if option == '1':
        pass
    elif option == '2':
        pass
    elif option == '3':
        pass
    elif option == '4':
        print("...Saliendo del programa...")
        time.sleep(1)
        break
    #Options
    else:
        print("Opción Inválida")
    print("...Presione una tecla para continuar...")
    msvcrt.getch()
#Menu