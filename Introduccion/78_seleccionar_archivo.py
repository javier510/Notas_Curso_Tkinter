import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicializarGui()
    
    def inicializarGui(self):
        self.title("Selector de archivos y carpetas")
        self.geometry("500x350")
        self.resizable(0,0)
        self.configure(bg='white')

        btn_sel_archivo = tk.Button(self, text="Seleccionar Archivo", command=self.seleccionarArchivo)
        btn_sel_archivo.pack(padx=60, pady=10)
        
        btn_sel_carpeta = tk.Button(self, text="Seleccionar Carpeta", command=self.seleccionarCarpeta)
        btn_sel_carpeta.pack(padx=60, pady=10)
    
    def seleccionarArchivo(self):
        tipos = (('Imagenes', '*.jpg *.png *.gif *.jpeg'), ('Textos planos', '*.txt'), ('Todos los archivos', '*.*'))

        archivo = fd.askopenfilename(title='Abrir archivo...', initialdir='/home/dell/Javier/Codigo/Python/4_proyectos/Zoom_In_Out_Generator/' , filetypes=tipos)
        if archivo:
            mb.showinfo('Mensaje: ', archivo)
    
    def seleccionarCarpeta(self):
        directorio = fd.askdirectory(title='Abrir carpeta...', initialdir='/home/dell/Javier/Codigo/Python/4_proyectos/Zoom_In_Out_Generator/')
        if directorio:
            mb.showinfo("Mensaje: ", directorio)
    
def main():
    app = Aplicacion()
    app.mainloop()

if __name__ == '__main__':
    main()