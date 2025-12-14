import tkinter as tk

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.title('Mostrar texto')
        self.geometry('500x360')

        self.lbl_saludo = tk.Label(self, text='Hola, Tk!', font=('Arial', 18), bg='black', fg='green')
        self.lbl_saludo.place(x=20, y=150)
    
def main():
    app = Aplicacion()
    app.mainloop()

if __name__=='__main__':
    main()