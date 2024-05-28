# Cesar/Cesaro/Ncrptd/Opciones/Op1.py
def encriptar(Txt, clave):# Funcion
    cifrado = ""
    for caracter in Txt:
        # Validaciones de mayuscula y minuscula
        if caracter.isalpha():
            desplazamiento = ord('A') if caracter.isupper() else ord('a')
            cifrado += chr((ord(caracter) - desplazamiento + clave) % 26 + desplazamiento)
        else:
            cifrado += caracter
    # imprime y reotarna        
    print("\nTexto encriptado:", cifrado)
    return cifrado
