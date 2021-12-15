from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
class histogram:
    def __init__(self, root, db):
        print("TAMOS")
        self.root = root
        self.db = db
        self.graph = Toplevel()
        fig, ax = plt.subplots()
        x, y = self.__get_data()
        ax.set_title('Especies de mascotas registradas')
        ax.set_ylabel("Cantidad")
        ax.set_xlabel("Especie")
        ax.bar(x, y, color = "blue")
        canvas = FigureCanvasTkAgg(fig, master = self.graph)
        canvas.draw()
        canvas.get_tk_widget().pack()
    def __get_data(self):
        sql = """SELECT especie.nom_esp, COUNT(mascota.id_especie)
                FROM mascota
                INNER JOIN especie ON mascota.id_especie = especie.id_especie
                GROUP BY mascota.id_especie;"""
        data = self.db.run_select(sql)
        x = [i[0] for i in data]
        y = [i[1] for i in data]
        return x, y
