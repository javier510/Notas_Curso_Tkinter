import tkinter as tk

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicializarGui()
    
    def inicializarGui(self):
        self.title('Introduccion Tkinter')
        self.geometry('500x360')

def main():
    app = Aplicacion()
    app.mainloop()

if __name__ == '__main__':
    main()