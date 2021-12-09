from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
class graficos:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.graph = Toplevel()
        fig, ax = plt.subplots()
        x, y = self.__get_data()
        ax.set_title('Número de jugadores por equipo')
        ax.set_ylabel("Jugadores")
        ax.set_xlabel("Equipos")
        ax.bar(x, y, color = "salmon")
        canvas = FigureCanvasTkAgg(fig, master = self.graph)  
        canvas.draw()
        canvas.get_tk_widget().pack()
    def __get_data(self):
        sql = """select equipo.nom_equipo, count(jugador.nom_jugador) from equipo
                join jugador on jugador.id_equipo = equipo.id_equipo 
                group by equipo.nom_equipo;"""
        data = self.db.run_select(sql)
        x = [i[0] for i in data]
        y = [i[1] for i in data]
        return x, y