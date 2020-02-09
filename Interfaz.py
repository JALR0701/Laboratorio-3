import tkinter as tk
import serial
import struct
import threading
import time
import queue

while(1):
    while(1):
        try:
            numero = str(int(input(">  COM: ")))
            port = "com" + numero
            break
        except:
            print ("Enter a numeric value")
    try:
        data = serial.Serial(port, baudrate = 9600, timeout=1500)
        break
    except:
        print("Unable to open port")
        
contador = 0
data.write(struct.pack('>B',contador))

def suma ():
    global contador
    contador = contador + 1
    if contador > 255:
        contador = 0
    data.write(struct.pack('>B',contador))
    sensor3.set(contador)
    return

def resta ():
    global contador
    contador = contador - 1
    if contador < 0:
        contador = 255
    data.write(struct.pack('>B',contador))
    sensor3.set(contador) 
    return

Main = tk.Tk()
Main.title("Comunicación serial")
w = 700 
h = 700

ws = Main.winfo_screenwidth()
hs = Main.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

Main.geometry('%dx%d+%d+%d' % (w, h, x, y))
Main.resizable(0,0)
Main. config (background = "Black")

com = tk.Label(Main, text = "COM:" + numero, bg = "black", fg = "white")
com.place(x = 50, y = 30)

sensor3 = tk.StringVar()
sensor3.set(contador)

ttl = tk.Label(Main, textvariable = sensor3, bg = "black", fg = "white")
ttl.place(x = 350, y = 250)

aumentar = tk.Button(Main, text = "+", command = suma)
aumentar.place(x = 400, y = 300)

decrementar = tk.Button(Main, text = "-", command = resta)
decrementar.place(x = 300, y = 300)

Main.mainloop()