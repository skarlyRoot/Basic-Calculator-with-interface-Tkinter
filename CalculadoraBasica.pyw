from tkinter import*
import tkinter as tk
import math
import os



ventana= Tk()
ventana.title("Calculadora-Basica") #.tittle para poner titulo superior el en programa
ventana.resizable(False, False)



ventana.config(bg="#282828")
fuente_negrita = ("Arial", 14, "bold")  # Cambiar a un valor numérico más alto
fuente_negrita = ("Arial", 14, 800) 
fuente_negrita = ("Impact", 18)

#Entrada
e_texto= Entry(ventana, justify="right",  bg="#282828", fg="green", borderwidth=2, relief="flat", font=("Calibri 18"), width=26)
e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=15)


#Columnspan spanea numero de columnas debajo del widge
#padx y pady es el espacio para el campo de texto

#Botones de numeracion

boton1= Button(ventana, text="1", width=5, height=2, command= lambda: click_boton(1), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton1.grid(row=4, column=0, padx=5, pady=5)

boton2= Button(ventana, text="2", width=5, height=2, command= lambda: click_boton(2), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton2.grid(row=4, column=1, padx=5, pady=5)

boton3= Button(ventana, text="3", width=5, height=2, command= lambda: click_boton(3), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton3.grid(row=4, column=2, padx=5, pady=5)

boton4= Button(ventana, text="4", width=5, height=2, command= lambda: click_boton(4), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton4.grid(row=3, column=0, padx=5, pady=5)

boton5= Button(ventana, text="5", width=5, height=2, command= lambda: click_boton(5), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton5.grid(row=3, column=1, padx=5, pady=5)

boton6= Button(ventana, text="6", width=5, height=2, command= lambda: click_boton(6), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton6.grid(row=3, column=2, padx=5, pady=5)

boton7= Button(ventana, text="7", width=5, height=2, command= lambda: click_boton(7), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton7.grid(row=2, column=0, padx=5, pady=5)

boton8= Button(ventana, text="8", width=5, height=2, command= lambda: click_boton(8), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton8.grid(row=2, column=1, padx=5, pady=5)

boton9= Button(ventana, text="9", width=5, height=2, command= lambda: click_boton(9), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton9.grid(row=2, column=2, padx=5, pady=5)

boton0= Button(ventana, text="0", width=12, height=2, command= lambda: click_boton(0), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton0.grid(row=5, column=0,columnspan=2, padx=5, pady=5)


#Botones de funciones

boton_Borrar= Button(ventana, text="⌫", width=5, height=2, command=lambda: borrar(), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton_Borrar.grid(row=1, column=3, padx=5, pady=5)

boton_raiz= Button(ventana, text="√", width=5, height=2, command= lambda: raiz(), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton_raiz.grid(row=1, column=1, padx=5, pady=5)

boton_exit= Button(ventana, text="Off", width=5, height=2, command= lambda: ventana.quit(), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton_exit.grid(row=1, column=0, padx=5, pady=5)

boton_div= Button(ventana, text="÷", width=5, height=2, command= lambda: click_boton("/"), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton_div.grid(row=1, column=2, padx=5, pady=5)

boton_punto= Button(ventana, text=".", width=5, height=2, command= lambda: click_boton("."), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton_punto.grid(row=5, column=2, padx=5, pady=5)

boton_multi= Button(ventana, text="X", width=5, height=2, command= lambda: click_boton("*"), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton_multi.grid(row=2, column=3, padx=5, pady=5)

boton_suma= Button(ventana, text="+", width=5, height=2, command= lambda: click_boton("+"), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton_suma.grid(row=4, column=3, padx=5, pady=5)

boton_resta= Button(ventana, text="-", width=5, height=2, command= lambda: click_boton("-"), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton_resta.grid(row=3, column=3, padx=5, pady=5)

boton_igual= Button(ventana, text="=", width=5, height=2, command= lambda: sol(), bg="#3b3939", fg="green",font= fuente_negrita, borderwidth=2, relief="flat")
boton_igual.grid(row=5, column=3, padx=5, pady=5)



#funcionalidad

i = 0

def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0, END)
    i = 0

def sol():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0



def raiz():
    ecuacion = e_texto.get()
    try:
        resultado = math.sqrt(float(ecuacion))
        e_texto.delete(0, END)
        e_texto.insert(0, resultado)
    except ValueError:
        e_texto.delete(0, END)
        e_texto.insert(0, "Error: Ingrese un número válido")















ventana.mainloop()