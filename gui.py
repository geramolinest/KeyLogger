import tkinter
from tkinter import Tk
import tkinter.filedialog as tf
import tkinter.messagebox as msg
import MC
from PIL import Image,ImageTk


def CenterScreen(width,height):
    x = (width/2) - (600/2)
    y = (height/2) - (600/2)
    return x,y
    

def Ventana():      
    window = Tk()
    window.title("AnonEncrypt")
    window.configure(bg = "white")
    #Tamaño de la ventana
    x,y = CenterScreen(window.winfo_screenwidth(),window.winfo_height())
    w = 600
    h = 600
    window.geometry('%dx%d+%d+%d' % (w, h, int(x), int(y)))  
    canvas = tkinter.Canvas(window,width=600,height = 600)
    canvas.grid(columnspan = 3,rowspan=3) 
    #Logo
    logo = Image.open("/home/anon23/Descargas/WallPapers/guy-fawkes-mask.png")
    logo = ImageTk.PhotoImage(logo)
     #Labels
    label  = tkinter.Label(image=logo)
    label.image = logo
    label.grid(column = 1,row = 0)
    #Button
    button = tkinter.Button(window,text = "Encrypt",command = Encrypt,bg = "#FFF779", width = 10,height = 3)
    button.grid(column = 0,row = 1)
    
    buttonD = tkinter.Button(window,text = "Decrypt", command = DesEncrypt,bg = "#9290FF",width = 10,height = 3)
    buttonD.grid(column = 2,row = 1)

    window.mainloop()

def DesEncrypt():
    try:      
        msg.showinfo("Llave","Seleccione llave para desencriptar")
        file_key = tf.askopenfilename()
        with open(file_key,'rb') as file:
            key = file.read()
        msg.showinfo("Directorio","Seleccione directorio a desencriptar")
        fileD = tf.askdirectory()
        MC.AnonNewsD(fileD,key)
        msg.showinfo("Encriptación","Se Desencriptó el directorio")
    except:
        msg.showerror("Encriptación","Error al desencriptar directorio")

def Encrypt():
    try:       
        mensaje = "Se generó un archivo con nombre Credenciales.txt\n" + "con la ruta del directorio que encriptó"
        
        fileD = tf.askdirectory()
        MC.AnonNews(fileD)
        msg.showinfo("Encriptación","Se encriptó el directorio")
        msg.showinfo("Atención",mensaje)
    except:
        msg.showerror("Encriptación","Error al encriptar directorio")   

if __name__ == '__main__':
    Ventana()




