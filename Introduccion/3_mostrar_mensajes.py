import tkinter as tk
from tkinter import messagebox as mb

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.title('Mostrar texto')
        self.geometry('500x360')

        mb.showinfo('Mensaje informativo: ', 'Hola, Tkinter!')
        mb.showwarning('Mensaje de advertencia', 'Revise todos los campos del formulario')
        mb.showerror('Mensaje de error', 'Hay problemas con la conexion a internet')
    
def main():
    app = Aplicacion()
    app.mainloop()

if __name__=='__main__':
    main()