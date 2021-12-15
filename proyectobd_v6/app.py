import tkinter as tk
from tkinter import Menu
from tkinter import LabelFrame, Label, Frame
from tkinter import Button
from PIL import Image, ImageTk

#
from database import Database
from medico import medico
from dueno import dueno
from pabellon import pabellon
from mascota import mascota
from jaula import jaula
from servicio import servicio
from especie import especie
from histogram import histogram
from histogram_2 import histogram_2
from graficos import graficos


class App:
    def __init__(self, db):
        self.db = db

        # Ventana principal
        self.root = tk.Tk()

        # Algunas especificaciones de tamaño y título de la ventana
        self.root.geometry("700x400")
        self.root.title("Veterinaria Patitas")

        self.__crea_menubar()
        self.__crea_botones_principales()
        self.__agrega_imagen_principal()

        # Empieza a correr la interfaz
        self.root.mainloop()

    # Barra de menú principal
    def __crea_menubar(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=False)

        file_menu.add_command (label='Salir',
                                command=self.root.destroy)

        menubar.add_cascade(label="Opciones", menu=file_menu)

    # Botones principales
    def __crea_botones_principales(self):
        padx = 2
        pady = 2

        frame = LabelFrame(self.root, text="Menú Princpal", relief=tk.GROOVE)
        frame.place(x=10, y=10, width=200, relheight=0.95)

        b1 = Button(frame, text="Médicos", width=20)
        b1.grid(row=2, column=0, padx=padx, pady=pady)
        b1.bind('<Button-1>', self.__mostrar_medicos)

        b2 = Button(frame, text="Jaulas", width=20)
        b2.grid(row=3, column=0, padx=padx, pady=pady)
        b2.bind('<Button-1>', self.__mostrar_jaulas)

        b3 = Button(frame, text="Dueños", width=20)
        b3.grid(row=4, column=0, padx=padx, pady=pady)
        b3.bind('<Button-1>', self.__mostrar_duenos)

        b4 = Button(frame, text="Mascotas", width=20)
        b4.grid(row=5, column=0, padx=padx, pady=pady)
        b4.bind('<Button-1>', self.__mostrar_mascotas)

        b9 = Button(frame, text="Especies", width=20)
        b9.grid(row=6, column=0, padx=padx, pady=pady)
        b9.bind('<Button-1>', self.__mostrar_especies)

        b5 = Button(frame, text="Servicio", width=20)
        b5.grid(row=7, column=0, padx=padx, pady=pady)
        b5.bind('<Button-1>', self.__mostrar_servicio)

        b6 = Button(frame, text="Gráfico Especies", width=20)
        b6.grid(row=8, column=0, padx=padx, pady=pady)
        b6.bind('<Button-1>', self.__mostrar_grafico)

        b7 = Button(frame, text="Gráfico Médico", width=20)
        b7.grid(row=9, column=0, padx=padx, pady=pady)
        b7.bind('<Button-1>', self.__mostrar_grafico_2)

        b8 = Button(frame, text="Gráficos", width=20)
        b8.grid(row=10, column=0, padx=padx, pady=pady)
        b8.bind('<Button-1>', self.__ventana_graficos)


        bg = Button(frame, text="Pabellón", width=20)
        bg.grid(row=11, column=0, padx=padx, pady=pady)
        bg.bind('<Button-1>', self.__mostrar_pabellon)

    # Imagen principal
    def __agrega_imagen_principal(self):
        #
        frame = LabelFrame(self.root, text="Cuidamos tu mascota, cuidamos tu familia", relief=tk.FLAT)
        frame.place(x=215, y=10, relwidth=0.68, relheight=0.95)

        image = Image.open("vet_logo.jpg")
        photo = ImageTk.PhotoImage(image.resize((450, 320), Image.ANTIALIAS))
        label = Label(frame, image=photo)
        label.image = photo
        label.pack()


    # Muestreo de ventanas
    def __mostrar_duenos(self, button):
        dueno(self.root, self.db)

    def __mostrar_medicos(self, button):
        medico(self.root, self.db)

    def __mostrar_mascotas(self, button):
        mascota(self.root, self.db)

    def __mostrar_jaulas(self, button):
        jaula(self.root, self.db)

    def __mostrar_especies(self, button):
        especie(self.root, self.db)

    def __mostrar_pabellon(self, button):
        pabellon(self.root, self.db)

    def __mostrar_servicio(self, button):
        servicio(self.root, self.db)

    def __mostrar_grafico(self, button):
        histogram(self.root, self.db)

    def __mostrar_grafico_2(self, button):
        histogram_2(self.root, self.db)

    def __ventana_graficos(self, button):
        graficos(self.root, self.db)

def main():
    # Conecta a la base de datos
    db = Database()

    # Llamado a la app
    App(db)

if __name__ == "__main__":
    main()
