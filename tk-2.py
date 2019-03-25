#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from tkinter import *    #  python 3.
except:
    from Tkinter import *    #  python 2.7
    
def main():

        #Crear y configurar ventana principal
        window = Tk() 
        window.title("Entry")         
        window.geometry('350x200')

        #widgets 
        lbl = Label(window, text="¿Cómo te llamas?")         
        lbl.grid(column=0, row=0)  #Colocar y Mostrar widget
         
        txt = Entry(window,width=10) # ancho en caracteres        
        txt.grid(column=1, row=0)  #Colocar y Mostrar widget

        hola = Label(window , text = '') #Label vacío
        hola.grid(column=3 , row=0)  #Colocar y Mostrar widget

         
        def clicked():         
            res = "Hola " + txt.get() # Leer valor introducido en Entry     GET()    
            hola.configure(text = res) # Modificar Label hola
         
        btn = Button(window, text="Aceptar", command=clicked)         
        btn.grid(column=2, row=0)  #Colocar y Mostrar widget

        #Bucle principal de la ventana 
        window.mainloop()

        
if __name__ == "__main__":       # averiguar si se está ejecutando o importando
        main()
