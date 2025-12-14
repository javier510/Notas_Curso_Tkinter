import tkinter as tk
from tkinter import messagebox as mb

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicializarGui()
    
    def inicializarGui(self):
        self.title('Mensaje y finalizar ventana')
        self.geometry('540x360')

        # Creamos una matriz filas y columnas de guia.
        for row in range(10):
            for col in range(7):
                btn_matriz = tk.Button(self, width=6, height=1)
                btn_matriz.grid(
                    row=row,
                    column=col
                )
        
        self.btn_saludar = tk.Button(self, text='Saludar', width=6, height=1, command=self.saludar)
        self.btn_saludar.grid(
            row=0,
            column=0,
            columnspan=2,
            rowspan=1,
            sticky='ew',
        )
        self.btn_salir = tk.Button(self, text='Salir', width=6, height=1, command=self.salir)
        self.btn_salir.grid(
            row=0,
            column=6,
            rowspan=1,
            columnspan=1,
            sticky='ew',
        )
    
    def saludar(self):
        mb.showinfo('Mensaje informativo', 'Hola desde Tkinter!')

    def salir(self):
        self.destroy()
    

def main():
    app = Aplicacion()
    app.mainloop()

if __name__ == '__main__':
    main()