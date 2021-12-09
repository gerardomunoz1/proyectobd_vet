import tkinter as tk
from tkinter import ttk


class medico:
    def __init__(self, root, db):
        self.db = db
        self.data = []

        # Toplevel es una ventana que está un nivel arriba que la principal
        self.root = tk.Toplevel()
        self.root.geometry('820x400')
        self.root.title("Medicos")
        self.root.resizable(width=0, height=0)

        # toplevel modal
        self.root.transient(root)

        #
        self.__config_treeview_medico()
        self.__config_buttons_medico()

    def __config_treeview_medico(self):
        self.treeview = ttk.Treeview(self.root)
        self.treeview.configure(columns=("#1", "#2", "#3"))
        self.treeview.heading("#0", text="Id")
        self.treeview.heading("#1", text="Nombre")
        self.treeview.heading("#2", text="Apellido")
        self.treeview.heading("#3", text="Fecha Ingreso")
        self.treeview.column("#0", minwidth=100, width=100, stretch=False)
        self.treeview.column("#1", minwidth=300, width=300, stretch=False)
        self.treeview.column("#2", minwidth=300, width=300, stretch=False)
        self.treeview.column("#3", minwidth=300, width=120, stretch=False)
        self.treeview.place(x=0, y=0, height=350, width=820)
        self.llenar_treeview_medico()
        self.root.after(0, self.llenar_treeview_medico)

    def __config_buttons_medico(self):
        tk.Button(self.root, text="Insertar Medico",
                  command=self.__insertar_medico).place(x=0, y=350, width=200, height=50)
        tk.Button(self.root, text="Modificar Medico",
                  command=self.__modificar_medico).place(x=200, y=350, width=200, height=50)
        tk.Button(self.root, text="Eliminar Medico",
                  command=self.__eliminar_jugador).place(x=400, y=350, width=200, height=50)


    # select  a la base de datos para obtener id, nombre, apellido, fecha ingreso del medico
    def llenar_treeview_medico(self):
        sql = """select id_medico, nom_med, ape_med, date_format(fecha_ingreso, "%Y-%m-%d")
        from medico;"""
        # obtiene los datos
        data = self.db.run_select(sql)
        print(data)

        if (data != self.data):
            self.treeview.delete(*self.treeview.get_children())  # Elimina todos los rows del treeview
            for i in data:
                self.treeview.insert("", "end", text=i[0],
                                     values=(i[1] + " " + i[2] + " " + i[3] ), iid=i[0], tags="rojo")
            self.data = data

    def __insertar_medico(self):
        insertar_medico(self.db, self)

    def __modificar_medico(self):
        if (self.treeview.focus() != ""):
            sql = """select id_medico, nom_med, ape_med, fecha_ingreso
            from medico where id_medico = %(id_medico)s"""

            row_data = self.db.run_select_filter(sql, {"id_medico": self.treeview.focus()})[0]
            modificar_medico(self.db, self, row_data)

    def __eliminar_jugador(self):
        sql = "delete from medico where id_medico = %(id_med)s"
        self.db.run_sql(sql, {"id_med": self.treeview.focus()})
        self.llenar_treeview_medico()


class insertar_medico:
    def __init__(self, db, padre):
        self.padre = padre
        self.db = db
        self.insert_datos = tk.Toplevel()
        self.__config_window()
        self.__config_label()
        self.__config_entry()
        self.__config_button()

    def __config_window(self):
        self.insert_datos.geometry('250x120')
        self.insert_datos.title("Insertar Medico")
        self.insert_datos.resizable(width=0, height=0)

    def __config_label(self):
        tk.Label(self.insert_datos, text="Nombre: ").place(x=10, y=10, width=90, height=20)
        tk.Label(self.insert_datos, text="Apellido: ").place(x=10, y=40, width=90, height=20)
        tk.Label(self.insert_datos, text="Fecha Ingreso ").place(x=10, y=70, width=90, height=20)

    def __config_entry(self):
        self.entry_nombre = tk.Entry(self.insert_datos)
        self.entry_nombre.place(x=110, y=10, width=90, height=20)
        self.entry_apellido = tk.Entry(self.insert_datos)
        self.entry_apellido.place(x=110, y=40, width=90, height=20)
        self.entry_fecha = tk.Entry(self.insert_datos)
        self.entry_fecha.place(x=110, y=70, width=90, height=20)

    def __config_button(self):
        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.__insertar).place(x=0, y=100, width=200, height=20)



    def __insertar(self):  # Insercion en la base de datos.
        sql = """insert medico (nom_med, ape_med, fecha_ingreso ) 
            values (%(nom_med)s, %(ape_med)s, %(fecha_ingreso)s)"""
        self.db.run_sql(sql, {"nom_med": self.entry_nombre.get(), "ape_med": self.entry_apellido.get(),
                              "fecha_ingreso": self.entry_fecha.get()})
        self.insert_datos.destroy()
        self.padre.llenar_treeview_medico()


class modificar_medico:
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
        self.insert_datos.geometry('250x120')
        self.insert_datos.title("Modificar Medico")
        self.insert_datos.resizable(width=0, height=0)

    def config_label(self):  # Labels
        tk.Label(self.insert_datos, text="Nombre: ").place(x=10, y=10, width=100, height=20)
        tk.Label(self.insert_datos, text="Apellido: ").place(x=10, y=40, width=100, height=20)
        tk.Label(self.insert_datos, text="Fecha Ingreso: ").place(x=10, y=70, width=100, height=20)

    def config_entry(self):  # Se configuran los inputs
        self.entry_nombre = tk.Entry(self.insert_datos)
        self.entry_nombre.place(x=110, y=10, width=90, height=20)
        self.entry_nombre.insert(0,self.row_data[1])
        self.entry_apellido = tk.Entry(self.insert_datos)
        self.entry_apellido.place(x=110, y=40, width=90, height=20)
        self.entry_apellido.insert(0,self.row_data[2])
        self.entry_fecha = tk.Entry(self.insert_datos)
        self.entry_fecha.place(x=110, y=70, width=90, height=20)
        self.entry_fecha.insert(0,self.row_data[3])

    def config_button(self):  # Botón aceptar, llama a la función modificar cuando es clickeado.
        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.modificar).place(x=0, y=100, width=200, height=20)

    def modificar(self):  # Insercion en la base de datos.
        sql = """update medico set nom_med = %(nom_med)s, ape_med = %(ape_med)s,
            fecha_ingreso = %(fecha_ingreso)s where id_medico = %(id_medico)s"""
        self.db.run_sql(sql, {"nom_med": self.entry_nombre.get(), "fecha_ingreso": self.entry_fecha.get(),
                              "ape_med": self.entry_apellido.get(), "id_medico": int(self.row_data[0])})
        self.insert_datos.destroy()
        self.padre.llenar_treeview_medico()


