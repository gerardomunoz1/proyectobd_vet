import tkinter as tk
from tkinter import ttk


class especie:
    def __init__(self, root, db):
        self.db = db
        self.data = []

        # Toplevel es una ventana que está un nivel arriba que la principal
        self.root = tk.Toplevel()
        self.root.geometry('1200x400')
        self.root.title("Especies registradas")
        self.root.resizable(width=0, height=0)

        # toplevel modal
        self.root.transient(root)

        #
        self.__config_treeview()
        self.__config_buttons()

    def __config_treeview(self):
        self.treeview = ttk.Treeview(self.root)
        self.treeview.configure(columns=("#1", "#2"))
        self.treeview.heading("#0", text="Id")
        self.treeview.heading("#1", text="Nombre especie")

        self.treeview.column("#0", minwidth=30, width=30, stretch=True)
        self.treeview.column("#1", minwidth=200, width=200, stretch=True)

        self.treeview.place(x=0, y=0, height=350, width=1199)

        self.llenar_treeview()
        self.root.after(0, self.llenar_treeview)

    def __config_buttons(self):

        tk.Button(self.root, text="Insertar Especie",
                  command=self.__insertar).place(x=0, y=350, width=200, height=50)
        tk.Button(self.root, text="Modificar Especie",
                  command=self.__modificar).place(x=200, y=350, width=200, height=50)
        tk.Button(self.root, text="Eliminar Especie",
                  command=self.__eliminar).place(x=400, y=350, width=200, height=50)

    # Relleno de treeview
    def llenar_treeview(self):
        sql = """SELECT especie.id_especie, especie.nom_esp FROM especie;"""

        # Obtiene los datos
        data = self.db.run_select(sql)
        print(data)

        if (data != self.data):
            self.treeview.delete(*self.treeview.get_children())  # Elimina todos los rows del treeview
            for i in data:
                self.treeview.insert("", "end", text=i[0],
                                     values=(i[1].replace(" ", "\\ " ) + " "), iid=i[0], tags="rojo")

            self.data = data

    def __insertar(self):
        insertar(self.db, self)

    def __modificar(self):
        if (self.treeview.focus() != ""): #id, especie

            sql = """SELECT especie.id_especie, especie.nom_esp FROM especie
                    WHERE especie.id_especie = %(id_especie)s;"""
            row_data = self.db.run_select_filter(sql, {"id_especie": self.treeview.focus()})[0]
            modificar(self.db, self, row_data)

    def __eliminar(self):
        sql = "DELETE FROM especie WHERE id_especie = %(id_especie)s"
        self.db.run_sql(sql, {"id_especie": self.treeview.focus()})
        self.llenar_treeview()


class insertar:
    def __init__(self, db, padre):
        self.padre = padre
        self.db = db
        self.insert_datos = tk.Toplevel()
        self.__config_window()
        self.__config_label()
        self.__config_entry()
        self.__config_button()

    def __config_window(self):
        self.insert_datos.geometry('400x200')
        self.insert_datos.title("Insertar Especie")
        self.insert_datos.resizable(width=0, height=0)

    def __config_label(self):#id, nombre, especie, dueño, descripcion, fecha

        tk.Label(self.insert_datos, text="Especie: ").place(x=10, y=40, width=150, height=20)

    def __config_entry(self):
        self.entry_nombre = tk.Entry(self.insert_datos)
        self.entry_nombre.place(x=160, y=10, width=200, height=20)


    def __config_button(self):
        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.__insertar).place(x=160, y=160, width=200, height=20)

    def __insertar(self):  # Insercion en la base de datos.
        sql = """INSERT INTO especie (nom_esp) VALUES (%(nom_esp)s);"""
        self.db.run_sql(sql, {"nom_esp": self.entry_nombre.get()})
        self.insert_datos.destroy()
        self.padre.llenar_treeview()

    def __fill_combo_especie(self):
        sql = "SELECT id_especie, nom_esp FROM especie"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_dueno(self):
        sql = "SELECT id_especie as id_especie from especie;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]


class modificar:
    def __init__(self, db, padre, row_data):
        self.padre = padre
        self.db = db
        self.row_data = row_data
        self.insert_datos = tk.Toplevel()
        self.config_window()
        self.config_label()
        self.config_entry()
        self.config_button()

    def config_window(self):  # Settings
        self.insert_datos.geometry('400x200')
        self.insert_datos.title("Modificar Especie")
        self.insert_datos.resizable(width=0, height=0)

    def config_label(self):  # Labels id, nombre especie

        tk.Label(self.insert_datos, text="Especie: ").place(x=10, y=40, width=100, height=20)

    def config_entry(self):  # Se configuran los inputs   #id, nombre especie
        self.entry_nombre = tk.Entry(self.insert_datos)
        self.entry_nombre.place(x=160, y=10, width=200, height=20)
        self.entry_nombre.insert(0, self.row_data[1])

    def config_button(self):  # Botón aceptar, llama a la función modificar cuando es clickeado.
        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.modificar).place(x=50, y=160, width=200, height=20)

    def modificar(self):  # Insercion en la base de datos.

        sql = """UPDATE especie SET nom_esp = %(nombre)s WHERE id_especie = %(id_especie)s"""
        self.db.run_sql(sql, {"nombre": self.entry_nombre.get(), "id_especie": int(self.row_data[0])})

        self.insert_datos.destroy()
        self.padre.llenar_treeview()

    def __fill_combo_especie(self):
        sql = "SELECT id_especie, nom_esp FROM especie"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_dueno(self):
        sql = "select id_dueno, concat(dueno.nom_due, ' ' , dueno.ape_due) as nombre from dueno;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]
