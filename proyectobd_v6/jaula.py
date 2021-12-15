import tkinter as tk
from tkinter import ttk


class jaula:
    def __init__(self, root, db):
        self.db = db
        self.data = []

        # Toplevel es una ventana que está un nivel arriba que la principal
        self.root = tk.Toplevel()
        self.root.geometry('640x400')
        self.root.title("Datos de Jaula")
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
        self.treeview.heading("#1", text="Descripción")

        self.treeview.column("#0", minwidth=30, width=30, stretch=True)
        self.treeview.column("#1", minwidth=200, width=200, stretch=True)

        self.treeview.place(x=0, y=0, height=350, width=1199)
        self.llenar_treeview()
        self.root.after(0, self.llenar_treeview)

    def __config_buttons(self):
        tk.Button(self.root, text="Insertar Jaula",
                  command=self.__insertar).place(x=0, y=350, width=200, height=50)
        tk.Button(self.root, text="Modificar Jaula",
                  command=self.__modificar).place(x=200, y=350, width=200, height=50)
        tk.Button(self.root, text="Eliminar Jaula",
                  command=self.__eliminar_jaula).place(x=400, y=350, width=200, height=50)

    # select  a la base de datos para obtener id, nombre, apellido, fecha ingreso del medico
    def llenar_treeview(self):

        sql = """SELECT id_jaula, descripcion FROM jaula;"""
        # obtiene los datos
        data = self.db.run_select(sql)
        print("[SQL] >", data)

        if (data != self.data):
            self.treeview.delete(*self.treeview.get_children())  # Elimina todos los rows del treeview
            for i in data:

                self.treeview.insert("", "end", text=i[0],
                                     values=(i[1].replace(" ", "\\ " ) + " "), iid=i[0], tags="rojo")

            self.data = data

    def __insertar(self):
        insertar(self.db, self)

    def __modificar(self):
        if (self.treeview.focus() != ""):
            sql = """SELECT id_jaula, descripcion FROM jaula;"""

            row_data = self.db.run_select_filter(sql, {"id_jaula": self.treeview.focus()})[0]
            modificar(self.db, self, row_data)
            print("[SQL MODIFICADO] >", row_data)

    def __eliminar_jaula(self):
        sql = "DELETE FROM jaula WHERE id_jaula = %(id_jaula)s"
        self.db.run_sql(sql, {"id_jaula": self.treeview.focus()})
        print("[SQL ELIMINADO CON ÉXITO]")
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
        self.insert_datos.geometry('350x200')
        self.insert_datos.title("Nueva Jaula")
        self.insert_datos.resizable(width=0, height=0)

    def __config_label(self):
        tk.Label(self.insert_datos, text="Descripción: ").place(x=10, y=10, width=90, height=20)


    def __config_entry(self):
        self.entry_nombre = tk.Entry(self.insert_datos)
        self.entry_nombre.place(x=110, y=10, width=200, height=20)

    def __config_button(self):
        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.__insertar).place(x=30, y=160, width=200, height=20)



    def __insertar(self):  # Insercion en la base de datos.
        sql = """INSERT INTO jaula (descripcion) VALUES (%(descripcion)s);"""

        self.db.run_sql(sql, {"descripcion": self.entry_nombre.get()})
        self.insert_datos.destroy()
        self.padre.llenar_treeview()


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
        self.insert_datos.geometry('350x200')
        self.insert_datos.title("Modificar Jaula")
        self.insert_datos.resizable(width=0, height=0)

    def config_label(self):  # Labels
        tk.Label(self.insert_datos, text="Descripción: ").place(x=10, y=10, width=100, height=20)

    def config_entry(self):  # Se configuran los inputs
        self.entry_nombre = tk.Entry(self.insert_datos)
        self.entry_nombre.place(x=110, y=10, width=200, height=20)
        self.entry_nombre.insert(0,self.row_data[1])

    def config_button(self):  # Botón aceptar, llama a la función modificar cuando es clickeado.
        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.modificar).place(x=50, y=160, width=200, height=20)

    def modificar(self):  # Insercion en la base de datos.
        sql = """UPDATE jaula SET descripcion = %(descripcion)s
                WHERE id_jaula = %(id_jaula)s;"""
        self.db.run_sql(sql, {"descripcion": self.entry_nombre.get(), "id_jaula": int(self.row_data[0])})
        self.insert_datos.destroy()
        self.padre.llenar_treeview()