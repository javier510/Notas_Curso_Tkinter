import tkinter as tk
from tkinter import messagebox as mb
from tkinter.ttk import Combobox

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicializarGui()
    
    def inicializarGui(self):
        self.title('Lista dezplegable')
        self.geometry('530x360')

        # Creamos una matriz de guia
        for row in range(10):
            for col in range(7):
                btn_matriz = tk.Button(self, width=6, height=1)
                btn_matriz.grid(
                    row=row,
                    column=col,
                )
        
        # Creamos la lista dezplegable
        lbl_seleccion = tk.Label(self, text='Seleccione lenguage favorito', width=6, height=1)
        lbl_seleccion.grid(
            row=0,
            column=0,
            rowspan=1,
            columnspan=3,
            sticky='ew'
        )

        self.cbx_languages = Combobox(self,
            values=['Python', 'C', 'C++', 'Java'],
            width=6,
            height=4
            )
        self.cbx_languages.grid(
            row=1,
            column=0,
            rowspan=1,
            columnspan=3,
            sticky='ew'
        )
        
        # Agregamos el boton salir.
        self.btn_salir = tk.Button(self, text='Salir', width=6, height=1, command=self.salir)
        self.btn_salir.grid(
            row=0,
            column=6,
            rowspan=1,
            columnspan=1,
            sticky='ew'
        )
        btn_mostrar_seleccion = tk.Button(self, text='Seleccionar', width=6, height=1, command=self.seleccionar)
        btn_mostrar_seleccion.grid(
            row=2,
            column=0,
            rowspan=1,
            columnspan=2,
            sticky='ew'
            )
    
    def seleccionar(self):
        language = self.cbx_languages.get()
        mb.showinfo('Mensaje Informativo', f'{language} es su lenguage favorito!')

    def salir(self):
        self.destroy()

def main():
    app = Aplicacion()
    app.mainloop()

if __name__ == '__main__':
    main()