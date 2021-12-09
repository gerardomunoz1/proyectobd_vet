import tkinter as tk
from tkinter import ttk


class dueno:
    def __init__(self, root, db):
        self.db = db
        self.data = []

        # Toplevel es una ventana que está un nivel arriba que la principal
        self.root = tk.Toplevel()
        self.root.geometry('1200x400')
        self.root.title("Datos del Dueño")
        self.root.resizable(width=0, height=0)

        # toplevel modal
        self.root.transient(root)

        #
        self.__config_treeview()
        self.__config_buttons()

    def __config_treeview(self):
        self.treeview = ttk.Treeview(self.root)
        self.treeview.configure(columns=("#1", "#2", "#3" , "#4", "#5"))
        self.treeview.heading("#0", text="Id")
        self.treeview.heading("#1", text="Nombre")
        self.treeview.heading("#2", text="Apellido")
        self.treeview.heading("#3", text="Telefono")
        self.treeview.heading("#4", text="Dirección")
        self.treeview.heading("#5", text="Email")
        self.treeview.column("#0", minwidth=30, width=30, stretch=False)
        self.treeview.column("#1", minwidth=200, width=200, stretch=False)
        self.treeview.column("#2", minwidth=200, width=200, stretch=False)
        self.treeview.column("#3", minwidth=200, width=200, stretch=False)
        self.treeview.column("#4", minwidth=200, width=300, stretch=False)
        self.treeview.column("#5", minwidth=200, width=300, stretch=False)
        self.treeview.place(x=0, y=0, height=350, width=1199)
        self.llenar_treeview()
        self.root.after(0, self.llenar_treeview)

    def __config_buttons(self):
        tk.Button(self.root, text="Insertar Dueño",
                  command=self.__insertar).place(x=0, y=350, width=200, height=50)
        tk.Button(self.root, text="Modificar Dueño",
                  command=self.__modificar).place(x=200, y=350, width=200, height=50)
        tk.Button(self.root, text="Eliminar Dueño",
                  command=self.__eliminar_jugador).place(x=400, y=350, width=200, height=50)


    # select  a la base de datos para obtener id, nombre, apellido, fecha ingreso del medico
    def llenar_treeview(self):
        sql = """select id_dueno, nom_due,ape_due,convert( telefono, char), direccion, email
        from dueno;"""
        # obtiene los datos
        data = self.db.run_select(sql)
        print(data)

        if (data != self.data):
            self.treeview.delete(*self.treeview.get_children())  # Elimina todos los rows del treeview
            for i in data:
                self.treeview.insert("", "end", text=i[0],
                                     values=(i[1] + " " + i[2] + " " + i[3] + " " + i[4]
                                             + " " + i[5]), iid=i[0], tags="rojo")
            self.data = data

    def __insertar(self):
        insertar(self.db, self)

    def __modificar(self):
        if (self.treeview.focus() != ""):
            sql = """select id_dueno, nom_due,ape_due,convert( telefono, char), direccion, email
        from dueno;"""

            row_data = self.db.run_select_filter(sql, {"id_due": self.treeview.focus()})[0]
            modificar(self.db, self, row_data)

    def __eliminar_jugador(self):
        sql = "delete from dueno where id_dueno = %(id_dueno)s"
        self.db.run_sql(sql, {"id_dueno": self.treeview.focus()})
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
        self.insert_datos.title("Insertar Dueño")
        self.insert_datos.resizable(width=0, height=0)

    def __config_label(self):
        tk.Label(self.insert_datos, text="Nombre: ").place(x=10, y=10, width=90, height=20)
        tk.Label(self.insert_datos, text="Apellido: ").place(x=10, y=40, width=90, height=20)
        tk.Label(self.insert_datos, text="Telefono: ").place(x=10, y=70, width=90, height=20)
        tk.Label(self.insert_datos, text="Dirección: ").place(x=10, y=100, width=90, height=20)
        tk.Label(self.insert_datos, text="Email: ").place(x=10, y=130, width=90, height=20)

    def __config_entry(self):
        self.entry_nombre = tk.Entry(self.insert_datos)
        self.entry_nombre.place(x=110, y=10, width=200, height=20)
        self.entry_apellido = tk.Entry(self.insert_datos)
        self.entry_apellido.place(x=110, y=40, width=200, height=20)
        self.entry_telefono = tk.Entry(self.insert_datos)
        self.entry_telefono.place(x=110, y=70, width=200, height=20)
        self.entry_direccion = tk.Entry(self.insert_datos)
        self.entry_direccion.place(x=110, y=100, width=200, height=20)
        self.entry_email = tk.Entry(self.insert_datos)
        self.entry_email.place(x=110, y=130, width=200, height=20)


    def __config_button(self):
        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.__insertar).place(x=30, y=160, width=200, height=20)



    def __insertar(self):  # Insercion en la base de datos.
        sql = """insert into dueno (nom_due, ape_due, telefono,direccion, email )
            values (%(nom_due)s, %(ape_due)s, %(telefono)s, %(direccion)s, %(email)s)"""
        self.db.run_sql(sql, {"nom_due": self.entry_nombre.get(), "ape_due": self.entry_apellido.get(),
                              "telefono": self.entry_telefono.get(), "direccion": self.entry_direccion.get(),
                              "email": self.entry_email.get() })
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
        self.insert_datos.title("Modificar Dueño")
        self.insert_datos.resizable(width=0, height=0)

    def config_label(self):  # Labels
        tk.Label(self.insert_datos, text="Nombre: ").place(x=10, y=10, width=100, height=20)
        tk.Label(self.insert_datos, text="Apellido: ").place(x=10, y=40, width=100, height=20)
        tk.Label(self.insert_datos, text="Telefono: ").place(x=10, y=70, width=100, height=20)
        tk.Label(self.insert_datos, text="Dirección: ").place(x=10, y=100, width=100, height=20)
        tk.Label(self.insert_datos, text="Email: ").place(x=10, y=130, width=100, height=20)

    def config_entry(self):  # Se configuran los inputs
        self.entry_nombre = tk.Entry(self.insert_datos)
        self.entry_nombre.place(x=110, y=10, width=200, height=20)
        self.entry_nombre.insert(0,self.row_data[1])
        self.entry_apellido = tk.Entry(self.insert_datos)
        self.entry_apellido.place(x=110, y=40, width=200, height=20)
        self.entry_apellido.insert(0,self.row_data[2])
        self.entry_telefono = tk.Entry(self.insert_datos)
        self.entry_telefono.place(x=110, y=70, width=200, height=20)
        self.entry_telefono.insert(0,self.row_data[3])
        self.entry_direccion = tk.Entry(self.insert_datos)
        self.entry_direccion.place(x=110, y=100, width=200, height=20)
        self.entry_direccion.insert(0,self.row_data[4])
        self.entry_email = tk.Entry(self.insert_datos)
        self.entry_email.place(x=110, y=130, width=200, height=20)
        self.entry_email.insert(0,self.row_data[5])


    def config_button(self):  # Botón aceptar, llama a la función modificar cuando es clickeado.
        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.modificar).place(x=50, y=160, width=200, height=20)

    def modificar(self):  # Insercion en la base de datos.
        sql = """update dueno set nom_due = %(nom_due)s, ape_due = %(ape_due)s,
            telefono = %(telefono)s, direccion = %(direccion)s, email = %(email)s where id_dueno = %(id_dueno)s"""
        self.db.run_sql(sql, {"nom_due": self.entry_nombre.get(), "direccion": self.entry_direccion.get(),
                              "ape_due": self.entry_apellido.get(), "email": self.entry_email.get(),
                              "telefono": int(self.entry_telefono.get()), "id_dueno": int(self.row_data[0])})

        self.insert_datos.destroy()
        self.padre.llenar_treeview()
