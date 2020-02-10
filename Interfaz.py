import tkinter as tk #Se importan las librerias a usar
import serial
import struct
import time

while(1): #Se inicializa la conexion con el puerto
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

Main = tk.Tk() #Se crea la vetana principal y sus caracteristicas
Main.title("Comunicación serial")
w = 500 
h = 200

ws = Main.winfo_screenwidth()
hs = Main.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

Main.geometry('%dx%d+%d+%d' % (w, h, x, y))
Main.resizable(0,0)
Main. config (background = "Black")

com = tk.Label(Main, text = "COM:" + numero, bg = "black", fg = "white", font = ("Times New Roman", 24)) #Label que muestra el COM utilizado
com.pack()

contador = 0
data.write(struct.pack('>B',contador)) #Se envian datos codificados por el puerto 

def getSensor(): #Funcion para leer el puerto continuamente
    if ord(data.read()) == 255: #Verificar y ordenar datos
        s11 = ord(data.read())
        s12 = ord(data.read())
        s21 = ord(data.read())
        s22 = ord(data.read())

        if s12 < 10: #Concatenar los valores 
            sensor1 = str(s11) + ".0" + str (s12) + "V"
            #print (sensor1)
        else:
            sensor1 = str(s11) + "." + str (s12) + "V"
            #print (sensor1)

        if s22 < 10:
            sensor2 = str(s21) + ".0" + str (s22) + "V"
            #print (sensor2)
        else:
            sensor2 = str(s21) + "." + str (s22) + "V"
            #print (sensor2)
            
        POT01.set(sensor1) #Definir el valor al texto variable de un label
        POT02.set(sensor2)
    Main.after(10, getSensor) #Tiempo en ms que se ejecuta esta funcion

def suma (): #Funcion suma
    global contador
    contador = contador + 1
    if contador > 255: #Contador de 8-bits
        contador = 0
    if contador >= 100:
        read3 = str(contador)
    elif contador >= 10 and contador < 100:
        read3 = "0" + str(contador)
    else:
        read3 = "00" + str(contador)
    data.write(struct.pack('>B',contador))
    sensor3.set(read3)

def resta (): #Funcion resta
    global contador
    contador = contador - 1
    if contador < 0:
        contador = 255
    if contador >= 100:
        read3 = str(contador)
    elif contador >= 10 and contador < 100:
        read3 = "0" + str(contador)
    else:
        read3 = "00" + str(contador)
    data.write(struct.pack('>B',contador))
    sensor3.set(read3)

name1 = tk.Label(Main, text = "POT01", bg = "black", fg = "white", font = ("Times New Roman", 14)) #Label de titulos
name1.place(x = 75, y = 50)

name2 = tk.Label(Main, text = "POT02", bg = "black", fg = "white", font = ("Times New Roman", 14))
name2.place(x = 220, y = 50)

name3 = tk.Label(Main, text = "TTL", bg = "black", fg = "white", font = ("Times New Roman", 14))
name3.place(x = 365, y = 50)

POT01 = tk.StringVar() #Declaracion de variable para texto
POT01.set("0")

read1 = tk.Label(Main, textvariable = POT01, bg = "black", fg = "white", font = ("OCR A Extended", 14)) #Label de texto variable para los pots
read1.place(x = 75, y = 100)

POT02 = tk.StringVar()
POT02.set("0")

read2 = tk.Label(Main, textvariable = POT02, bg = "black", fg = "white", font = ("OCR A Extended", 14))
read2.place(x = 220, y = 100)

sensor3 = tk.StringVar()
sensor3.set("000")

read3 = tk.Label(Main, textvariable = sensor3, bg = "black", fg = "white", font = ("OCR A Extended", 14))
read3.place(x = 365, y = 100)

aumentar = tk.Button(Main, text = "+", command = suma) #Boton enlazado con la funcion suma
aumentar.place(x = 400, y = 150)

decrementar = tk.Button(Main, text = "-", command = resta) #Boton enlazado con la funcion resta
decrementar.place(x = 365, y = 150)

Main.after(10, getSensor)

Main.mainloop()
