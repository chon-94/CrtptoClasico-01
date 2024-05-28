# main.py
from Ncrptd.Menu import principal, Encriptado
from Ncrptd.Opciones.Op0 import clave as solicitar_clave
from Ncrptd.Opciones.Op1 import encriptar
from Ncrptd.Opciones.Op2 import decriptar

def main():# Funcion

    # Iniciando varaibles
    clave = None  
    texto_cifrado = "" 

    # Bucle Inicial
    while True:
        principal()
        opcion = input("Seleccionar: ")

        if opcion == '1':
            Txt = input('Ingresar texto -> ')
            while True:
                Encriptado()
                sub_opcion = input("Seleccionar: ")
                if sub_opcion == '1':
                    clave = solicitar_clave()  
                elif sub_opcion == '2':
                    if clave is not None:  
                        texto_cifrado = encriptar(Txt, clave)
                    else:
                        print("\nNo se ha ingresado una clave. ")
                elif sub_opcion == '3':
                    if texto_cifrado:
                        decriptar(texto_cifrado)
                    else:
                        print("\nNo hay texto cifrado disponible.")
                elif sub_opcion == '4':
                    break
                else:
                    print("\nOpción no válida. Por favor.")
        elif opcion == '2':
            print("Saliendo del programa...")
            break
        else:
            print("\nOpción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()
