#Libraries
import os, time, msvcrt
from functions import *
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
        comprar_entrada()
    elif option == '2':
        consultar_comprador()
    elif option == '3':
        cancelar_compra()
    elif option == '4':
        print("...Programa terminado...")
        time.sleep(1)
        break
    #Options
    else:
        print("¡Debe ingresar una opción válida!")
    print("...Presione una tecla para continuar...")
    msvcrt.getch()
#Menu