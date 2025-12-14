import tkinter as tk
from tkinter import messagebox as mb

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.title('Capturar datos')
        self.geometry('530x360')

        # Creamos la matriz
        for row in range(10):
            for col in range(7):
                btn_matriz = tk.Button(self, width=6, height=1)
                btn_matriz.grid(
                    row=row,
                    column=col
                )
        
        # Creamos un label que muestre el campo 'Nombre'
        lbl_nombre = tk.Label(self, text='Nombre', width=6, height=1)
        lbl_nombre.grid(row=0,
                        column=0,
                        rowspan=1,
                        columnspan=2,
                        sticky='ew'
                        )
        
        
        self.txt_nombre = tk.Entry(self, width=18)
        self.txt_nombre.grid(
            row=0,
            column=2,
            rowspan=1,
            columnspan=2,
            sticky='ew'
        )

        self.btn_saludar = tk.Button(self, text='Saludar', width=6, height=1, command=self.saludar)
        self.btn_saludar.grid(
            row=0,
            column=4,
            rowspan=1,
            columnspan=1,
            sticky='ew'
        )

        self.btn_salir = tk.Button(self, text='Salir', width=6, height=1, command=self.salir)
        self.btn_salir.grid(
            row=0,
            column=6,
            rowspan=1,
            columnspan=1,
            sticky='ew'
        )
    
    def saludar(self):
        nombre = self.txt_nombre.get()
        if len(nombre):
            mb.showinfo('Mensaje informativo', f'Hola, {nombre}!!')
        else:
            mb.showwarning('Mensaje Advertencia', f'Debe escribir un nombre')
    
    def salir(self):
        self.destroy()
    
def main():
    app = Aplicacion()
    app.mainloop()

if __name__ == '__main__':
    main()