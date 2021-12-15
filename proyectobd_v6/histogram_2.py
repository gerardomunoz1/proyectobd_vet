from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

class histogram_2:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.graph = Toplevel()
        fig, ax = plt.subplots()
        x, y = self.__get_data()
        ax.set_title('Tipo de especies atendidos por médico')
        ax.set_ylabel("Cantidad")
        ax.set_xlabel("Médico")
        ax.bar(y, x, color = "purple")
        canvas = FigureCanvasTkAgg(fig, master = self.graph)
        canvas.draw()
        canvas.get_tk_widget().pack()
    def __get_data(self):
        sql = """SELECT e.id_especie, e.nom_esp, m2.id_medico, CONCAT(m2.nom_med, ' ', m2.ape_med)
                 AS Nombre_apellido_Medico
                 FROM especie e JOIN mascota m ON e.id_especie = m.id_especie
                 JOIN servicio s ON m.id_mascota = s.id_mascota
                 JOIN realizado_por rp ON s.id_servicio = rp.id_servicio
                 JOIN medico m2 ON rp.id_medico = m2.id_medico;"""

        data = self.db.run_select(sql)

        x = [i[0] for i in data]
        y = [i[3] for i in data]

        print("X linea:", x)
        print("Y linea:", y)
        return x, y
