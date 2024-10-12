import tkinter as tk

def convertir():
    try:
        #obtiene el valor ingresado en el campo de entrada
        kilometros = float(entrada_kilometros.get())
        
        #realiza la conversion a millas 1KM = 0.621371 millas
        millas = kilometros * 0.621371
        
        #Actualiza la etiqueta de resultado
        etiqueta_resultado.config(text=f"{kilometros} kilometros son {millas} millas")
    except ValueError:
        #Manejo de errores para entradas no validas
        etiqueta_resultado.config(text="Ingrese un valor numerico valido")

# crear ventana principal
ventana= tk.Tk()
ventana.title("Conversor de kilometros a millas")
ventana.geometry("300x150") #establece el tamaño de la ventana

#crea etiqueta de instruccion y comocarla en la cuadricula
etiqueta_instruccion = tk.Label(ventana, text="Ingrese la distancia en kilometros: ")
etiqueta_instruccion.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#crear campo de entrada y colocarlo en la cuadricula
entrada_kilometros = tk.Entry(ventana)
entrada_kilometros.grid(row=1, column=0, padx=10, pady=10)

#crear boton de conversiob y ponerlo en la cuadricula
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.grid(row=1, column=1, padx=10, pady=10)

#crear etiqueta de resultado y colocarla en la cuadricula
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#inicia la aplicacion
ventana.mainloop()

