# Cesar/Cesaro/Ncrptd/Opciones/Op3.py
# def aplicar_rejilla(texto, filas, columnas):
#     # Crear una cuadrícula vacía
#     rejilla = [['' for _ in range(columnas)] for _ in range(filas)]
    
#     # Rellenar la rejilla con el texto
#     index = 0
#     for i in range(filas):
#         for j in range(columnas):
#             if index < len(texto):
#                 rejilla[i][j] = texto[index]
#                 index += 1
    
#     # Leer la rejilla en un orden diferente (por columnas en este caso)
#     texto_reorganizado = ''
#     for j in range(columnas):
#         for i in range(filas):
#             if rejilla[i][j]:
#                 texto_reorganizado += rejilla[i][j]
    
#     return texto_reorganizado

# def encriptar_con_rejilla(texto, clave, filas, columnas):
#     texto_cifrado = encriptar(texto, clave)
#     texto_reorganizado = aplicar_rejilla(texto_cifrado, filas, columnas)
#     print("\nTexto encriptado con rejilla:", texto_reorganizado)
#     return texto_reorganizado
