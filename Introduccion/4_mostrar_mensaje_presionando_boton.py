import tkinter as tk
from tkinter import messagebox as mb

class Aplicacion(tk.Tk):
    # Definimos constantes para ancho y alto de la ventana.
    ANCHO_VENTANA = 500
    ALTO_VENTANA = 360

    def __init__(self):
        super().__init__()
        self.inicializarGui()
    
    def inicializarGui(self):
        self.title('Asociar mensaje informativo al evento')
        self.geometry(f'{self.ANCHO_VENTANA}x{self.ALTO_VENTANA}')

        for row in range(10):
            for col in range(7):
                tk.Button(
                    self,
                    width=6,
                    height=1,
                ).grid(row=row, column=col)
        
        tk.Button(self, text="Saludar", width=6, height=1, command=self.saludar).grid(
            row=4,
            column=1,
            columnspan=1,
            rowspan=1,
            sticky="ew",
        )
        #self.btn_saludar.pack(pady=100)
        #self.btn_saludar.place(x=40, y=self.ALTO_VENTANA/3)
    
    def saludar(self):
        mb.showinfo('Mensaje informativo', 'Hola desde Tkinter!')
    
def main():
    app = Aplicacion()
    app.mainloop()

if __name__ == '__main__':
    main()