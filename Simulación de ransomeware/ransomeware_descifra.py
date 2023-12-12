import os
from ransomeware import get_key,decrypt

try:
    # Directorio a descifrar.
    path_to_decrypt = './Victima'

    # eliminamos el archivo típico con el mensaje solicitando el rescate.
    os.remove('./mensajeVictima.txt')

    # archvios del directorio para su descifrado y se guarda en una lista.
    items = os.listdir(path_to_decrypt)
    full_path_files = [path_to_decrypt + '/' + item for item in items]

    # Obtener la key utiliada para el cifrado.
    key = get_key()
    # Un vez tengamos la clave hay que destruirla 
    os.remove('./clave.key')
    # Desciframos los archivos afectados.
    decrypt(full_path_files, key)

except:
    print("Occurrió algún error inesperado!!!!!")