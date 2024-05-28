# Cesar/Cesaro/Ncrptd/Opciones/Op2.py
def decriptar(texto_cifrado):# Funcion
    # ingresar los digitos
    clave = int(input("Ingrese clave de descifrado -> "))
    descifrado = "" # <-variable vacia
    # # Itera sobre cada carácter en el texto cifrado.
    for caracter in texto_cifrado:
        # Validaciones de mayuscula y minuscula
        if caracter.isalpha():
            desplazamiento = ord('A') if caracter.isupper() else ord('a')# Cifrado en mayuscula y minuscula
            descifrado += chr((ord(caracter) - desplazamiento - clave) % 26 + desplazamiento)
        else:
            # Si el carácter no es una letra, se añade al resultado sin cambios.
            descifrado += caracter
    print("\nTexto descifrado:", descifrado)
    return descifrado

