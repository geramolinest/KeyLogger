from cryptography.fernet import Fernet
import os 
import Anon as a

def decrypt(items,key):
    f = Fernet(key)
    for item in items:
        with open(item,'rb') as file:
            if "README.txt" in item:
                continue                   
            encrypted_data = file.read()       
        decrypted_data = f.decrypt(encrypted_data)
        with open(item,'wb') as file:
            file.write(decrypted_data)

if __name__ == '__main__':
    path_to_encrypt = '/home/anon23/Descargas/RansomWare/Files'
   
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt + '/' + item for item in items]
    print('Introduzca su llave para desencriptar')
    key = a.cargar_key()
    decrypt(full_path,key)
    if os.path.exists(path_to_encrypt + '/README.txt'):
        os.remove(path_to_encrypt + '/README.txt')   
