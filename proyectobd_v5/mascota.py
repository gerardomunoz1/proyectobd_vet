import tkinter as tk
from tkinter import ttk


class mascota:
    def __init__(self, root, db):
        self.db = db
        self.data = []

        # Toplevel es una ventana que está un nivel arriba que la principal
        self.root = tk.Toplevel()
        self.root.geometry('1200x400')
        self.root.title("Datos de la mascota")
        self.root.resizable(width=0, height=0)

        # toplevel modal
        self.root.transient(root)

        #
        self.__config_treeview()
        self.__config_buttons()

    def __config_treeview(self):
        self.treeview = ttk.Treeview(self.root)
        self.treeview.configure(columns=("#1", "#2", "#3", "#4", "#5"))
        self.treeview.heading("#0", text="Id")
        self.treeview.heading("#1", text="Nombre")
        self.treeview.heading("#2", text="Especie")
        self.treeview.heading("#3", text="Dueño")
        self.treeview.heading("#4", text="Descripcion")
        self.treeview.heading("#5", text="Fecha nacimiento")
        self.treeview.column("#0", minwidth=30, width=30, stretch=False)
        self.treeview.column("#1", minwidth=200, width=200, stretch=False)
        self.treeview.column("#2", minwidth=200, width=200, stretch=False)
        self.treeview.column("#3", minwidth=100, width=200, stretch=False)
        self.treeview.column("#4", minwidth=100, width=300, stretch=False)
        self.treeview.column("#5", minwidth=400, width=300, stretch=False)
        self.treeview.place(x=0, y=0, height=350, width=1199)
        self.llenar_treeview()
        self.root.after(0, self.llenar_treeview)

    def __config_buttons(self):
        tk.Button(self.root, text="Insertar Mascota",
                  command=self.__insertar).place(x=0, y=350, width=200, height=50)
        tk.Button(self.root, text="Modificar Mascota",
                  command=self.__modificar).place(x=200, y=350, width=200, height=50)
        tk.Button(self.root, text="Eliminar Mascota",
                  command=self.__eliminar).place(x=400, y=350, width=200, height=50)

    # select  a la base de datos para obtener id, nombre, apellido, fecha ingreso del medico
    def llenar_treeview(self):
        sql = """select mascota.id_mascota, mascota.nom_masc, especie.nom_esp, concat( dueno.nom_due,' ', 
        dueno.ape_due) as nombre , mascota.descrip_masc, date_format(mascota.fecha_nacimiento, "%Y-%m-%d")
        from mascota join dueno on mascota.id_dueno = dueno.id_dueno
         join especie  on mascota.id_especie = especie.id_especie ;"""
        # obtiene los datos
        data = self.db.run_select(sql)
        print(data)

        if (data != self.data):
            self.treeview.delete(*self.treeview.get_children())  # Elimina todos los rows del treeview
            for i in data:
                self.treeview.insert("", "end", text=i[0],
                                     values=(i[1].replace(" ", "\\ ") + " " + i[2] + " " + i[3].replace(" ", "\\ ") +
                                             " " + i[4].replace(" ", "\\ ") + " " + i[5]), iid=i[0], tags="rojo")

            self.data = data

    def __insertar(self):
        insertar(self.db, self)

    def __modificar(self):
        if (self.treeview.focus() != ""): #id, nombre, especie, dueño, descripcion, fecha
            sql = """select mascota.id_mascota, mascota.nom_masc, especie.nom_esp, concat( dueno.nom_due,' ', 
            dueno.ape_due) as nombre , mascota.descrip_masc, date_format(mascota.fecha_nacimiento, "%Y-%m-%d")
            from mascota join dueno on mascota.id_dueno = dueno.id_dueno
            join especie  on mascota.id_especie = especie.id_especie where mascota.id_mascota = %(id_mascota)s;"""

            row_data = self.db.run_select_filter(sql, {"id_mascota": self.treeview.focus()})[0]
            modificar(self.db, self, row_data)

    def __eliminar(self):
        sql = "delete from mascota where id_mascota = %(id_mascota)s"
        self.db.run_sql(sql, {"id_mascota": self.treeview.focus()})
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
        self.insert_datos.title("Insertar Mascota")
        self.insert_datos.resizable(width=0, height=0)

    def __config_label(self):#id, nombre, especie, dueño, descripcion, fecha
        tk.Label(self.insert_datos, text="Nombre: ").place(x=10, y=10, width=150, height=20)
        tk.Label(self.insert_datos, text="Especie: ").place(x=10, y=40, width=150, height=20)
        tk.Label(self.insert_datos, text="Dueño: ").place(x=10, y=70, width=150, height=20)
        tk.Label(self.insert_datos, text="Descripción: ").place(x=10, y=100, width=150, height=20)
        tk.Label(self.insert_datos, text="Fecha Nacimiento: ").place(x=10, y=130, width=150, height=20)

    def __config_entry(self):
        self.entry_nombre = tk.Entry(self.insert_datos)
        self.entry_nombre.place(x=160, y=10, width=200, height=20)
        self.combo_especie = ttk.Combobox(self.insert_datos)
        self.combo_especie.place(x=160, y=40, width=200, height=20)
        self.combo_especie["values"], self.id_esp = self.__fill_combo_especie()
        self.combo_dueno = ttk.Combobox(self.insert_datos)
        self.combo_dueno.place(x=160, y=70, width=200, height=20)
        self.combo_dueno["values"], self.id_due = self.__fill_combo_dueno()
        self.entry_descripcion = tk.Entry(self.insert_datos)
        self.entry_descripcion.place(x=160, y=100, width=200, height=20)
        self.entry_fecha= tk.Entry(self.insert_datos)
        self.entry_fecha.place(x=160, y=130, width=200, height=20)

    def __config_button(self):
        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.__insertar).place(x=160, y=160, width=200, height=20)

    def __insertar(self):  # Insercion en la base de datos.
        sql = """insert into mascota (nom_masc, id_especie, id_dueno, descrip_masc, fecha_nacimiento ) 
            values (%(nom_mascota)s, %(id_especie)s, %(id_dueno)s, %(descrip_masc)s, %(fecha)s)"""
        self.db.run_sql(sql, {"nom_mascota": self.entry_nombre.get(), "id_especie": self.id_esp[self.combo_especie.current()],
                              "id_dueno": self.id_due[self.combo_dueno.current()], "descrip_masc": self.entry_descripcion.get(),
                              "fecha": self.entry_fecha.get()})
        self.insert_datos.destroy()
        self.padre.llenar_treeview()

    def __fill_combo_especie(self):
        sql = "select id_especie, nom_esp from especie"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_dueno(self):
        sql = "select id_dueno, concat(dueno.nom_due, ' ' , dueno.ape_due) as nombre from dueno;"
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
        self.insert_datos.title("Modificar Datos de Mascota")
        self.insert_datos.resizable(width=0, height=0)

    def config_label(self):  # Labels id, nombre, especie, dueño, descripcion, fecha
        tk.Label(self.insert_datos, text="Nombre: ").place(x=10, y=10, width=100, height=20)
        tk.Label(self.insert_datos, text="Especie: ").place(x=10, y=40, width=100, height=20)
        tk.Label(self.insert_datos, text="Dueño: ").place(x=10, y=70, width=100, height=20)
        tk.Label(self.insert_datos, text="Descripción: ").place(x=10, y=100, width=100, height=20)
        tk.Label(self.insert_datos, text="Fecha: ").place(x=10, y=130, width=100, height=20)

    def config_entry(self):  # Se configuran los inputs   #id, nombre, especie, dueño, descripcion, fecha
        self.entry_nombre = tk.Entry(self.insert_datos)
        self.entry_nombre.place(x=160, y=10, width=200, height=20)
        self.entry_nombre.insert(0, self.row_data[1])
        self.combo_especie = ttk.Combobox(self.insert_datos)
        self.combo_especie.place(x=160, y=40, width=200, height=20)
        self.combo_especie["values"], self.id_esp = self.__fill_combo_especie()
        self.combo_especie.insert(0, self.row_data[2])
        self.combo_dueno = ttk.Combobox(self.insert_datos)
        self.combo_dueno.place(x=160, y=70, width=200, height=20)
        self.combo_dueno["values"], self.id_due = self.__fill_combo_dueno()
        self.combo_dueno.insert(0, self.row_data[3])
        self.entry_descripcion = tk.Entry(self.insert_datos)
        self.entry_descripcion.place(x=160, y=100, width=200, height=20)
        self.entry_descripcion.insert(0, self.row_data[4])
        self.entry_fecha= tk.Entry(self.insert_datos)
        self.entry_fecha.place(x=160, y=130, width=200, height=20)
        self.entry_fecha.insert(0, self.row_data[5])

    def config_button(self):  # Botón aceptar, llama a la función modificar cuando es clickeado.
        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.modificar).place(x=50, y=160, width=200, height=20)

    def modificar(self):  # Insercion en la base de datos.

        sql = """update mascota set nom_masc = %(nombre)s, id_especie = %(especie)s,
                    id_dueno = %(dueno)s, descrip_masc = %(descripcion)s, fecha_nacimiento = %(fecha)s where id_mascota = %(id_mascota)s"""
        self.db.run_sql(sql, {"nombre": self.entry_nombre.get(), "especie": int(self.id_esp[ self.combo_especie.current()]),
                              "dueno": int(self.id_due[self.combo_dueno.current()]), "descripcion": self.entry_descripcion.get(),
                              "fecha": self.entry_fecha.get(), "id_mascota": int(self.row_data[0])})

        self.insert_datos.destroy()
        self.padre.llenar_treeview()

    def __fill_combo_especie(self):
        sql = "select id_especie, nom_esp from especie"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_dueno(self):
        sql = "select id_dueno, concat(dueno.nom_due, ' ' , dueno.ape_due) as nombre from dueno;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]


