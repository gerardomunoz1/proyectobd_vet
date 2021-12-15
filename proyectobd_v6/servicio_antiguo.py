import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class servicio:
    def __init__(self, root, db):
        self.db = db
        self.data = []
        self.ancho = 600
        self.alto = 400
        self.__ancho = self.ancho / 10
        self.__alto = self.alto / 10

        # Toplevel es una ventana que está un nivel arriba que la principal
        self.root = tk.Toplevel()
        self.root.geometry('%dx%d' % (self.ancho, self.alto))
        self.root.title("Servicio")
        self.root.resizable(width=0, height=0)

        # toplevel modal
        self.root.transient(root)

        # llama a los botones
        self.__config_buttons()

    def __config_buttons(self):
        tk.Button(self.root, text="Ingresar",
                  command=self.__insertar).place(x=2 * self.__ancho, y=1 * self.__alto, width=2 * self.__ancho,
                                                 height=2 * self.__alto)
        tk.Button(self.root, text="Buscar",
                  command=self.__insertar).place(x=6 * self.__ancho, y=1 * self.__alto, width=2 * self.__ancho,
                                                 height=2 * self.__alto)
        tk.Button(self.root, text="Eliminar",
                  command=self.__insertar).place(x=2 * self.__ancho, y=4 * self.__alto, width=2 * self.__ancho,
                                                 height=2 * self.__alto)
        tk.Button(self.root, text="Ver Todo",
                  command=self.__insertar).place(x=6 * self.__ancho, y=4 * self.__alto, width=2 * self.__ancho,
                                                 height=2 * self.__alto)
        tk.Button(self.root, text="Volver Atrás",
                  command=self.__insertar).place(x=4 * self.__ancho, y=7 * self.__alto, width=2 * self.__ancho,
                                                 height=2 * self.__alto)

    def __insertar(self):
        insertar(self.db, self)

    def __modificar(self):
        if (self.treeview.focus() != ""):  # id, nombre, especie, dueño, descripcion, fecha
            sql = """select mascota.id_mascota, mascota.nom_masc, especie.nom_esp, concat( dueno.nom_due,' ', 
            dueno.ape_due) as nombre , mascota.descrip_masc, date_format(mascota.fecha_nacimiento, "%Y-%m-%d")
            from mascota join dueno on mascota.id_dueno = dueno.id_dueno
            join especie  on mascota.id_especie = especie.id_especie where mascota.id_mascota = %(id_mascota)s;"""

    def __eliminar(self):
        sql = "delete from mascota where id_mascota = %(id_mascota)s"


class insertar:
    def __init__(self, db, padre):
        self.padre = padre
        self.db = db
        self.insert_datos = tk.Toplevel()
        self.__config_window()
        self.__config_label()
        self.__config_entry()
        self.__checkBotton()
        self.__config_button()

    def __config_window(self):
        self.insert_datos.geometry('500x600')
        self.insert_datos.title("Insertar Mascota")
        self.insert_datos.resizable(width=0, height=0)

    def __config_label(self):  # id, nombre, especie, dueño, descripcion, fecha

        padx = 2
        pady = 5

        self.insert_datos.grid_columnconfigure(10, minsize=100)

        tk.Label(self.insert_datos, text="DATOS MASCOTA", font=("helvetica 9 bold")).grid(row=0, column=0, padx=padx,
                                                                                          pady=pady, columnspan=2,
                                                                                          sticky="NW")
        tk.Label(self.insert_datos, text="  Mascota: ").grid(row=1, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="  Peso: ").grid(row=2, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="DIAGNÓSTICO", font=("helvetica 9 bold")).grid(row=3, column=0, padx=padx,
                                                                                        pady=pady, columnspan=2,
                                                                                        sticky="NW")
        tk.Label(self.insert_datos, text="  Nombre: ").grid(row=4, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="  Observaciones: ").grid(row=5, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="MÉDICO", font=("helvetica 9 bold")).grid(row=6, column=0, padx=padx,
                                                                                   pady=pady, columnspan=2, sticky="NW")
        tk.Label(self.insert_datos, text="  Nombre: ").grid(row=7, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="USO DE INSTALACIONES", font=("helvetica 9 bold")).grid(row=8, column=0,
                                                                                                 pady=pady,
                                                                                                 columnspan=2,
                                                                                                 sticky="NW")
        tk.Label(self.insert_datos, text="Tipo de Jaula :").grid(row=10, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Fecha :").grid(row=11, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Cantidad de dias:").grid(row=12, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Tipo dd pabelLon:").grid(row=15, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Fecha :").grid(row=16, column=0, padx=padx, pady=pady, sticky="W")

        tk.Label(self.insert_datos, text="\n").grid(row=16, column=0, padx=padx, pady=pady,
                                                    ipady=10)  # row vacio para generar espacio

    def __checkBotton(self):
        var_jaula = tk.IntVar()
        var_pabellon = tk.IntVar()

        chk_jaula = tk.Checkbutton(self.insert_datos, text=' Uso de Jaula', variable=var_jaula, onvalue=1)
        chk_jaula.grid(row=9, column=0, pady=5, padx=2, sticky="SW")
        chk_pabellon = tk.Checkbutton(self.insert_datos, text=' Uso de Jaula', variable=var_pabellon, onvalue=1)
        chk_pabellon.grid(row=13, column=0, pady=5, padx=2, sticky="SW")

    def __config_entry(self):
        padx = 2
        pady = 2

        self.combo_mascota = ttk.Combobox(self.insert_datos)
        self.combo_mascota.grid(row=1, column=1, ipadx=90, pady=pady, padx=padx, sticky="W")
        self.combo_mascota["values"], self.id_masc = self.__fill_combo_mascota()
        self.entry_peso = tk.Entry(self.insert_datos)
        self.entry_peso.grid(row=2, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_diagnostico = ttk.Combobox(self.insert_datos)
        self.combo_diagnostico.grid(row=4, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_diagnostico["values"], self.id_diag = self.__fill_combo_diagnostico()
        self.entry_observaciones = tk.Entry(self.insert_datos)
        self.entry_observaciones.grid(row=5, column=1, pady=pady, padx=padx, ipadx=90, sticky="W")
        self.combo_medico = ttk.Combobox(self.insert_datos)
        self.combo_medico.grid(row=7, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_medico["values"], self.id_med = self.__fill_combo_medico()
        self.combo_jaula = ttk.Combobox(self.insert_datos)
        self.combo_jaula.grid(row=10, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_jaula["values"], self.id_jau = self.__fill_combo_jaula()
        self.entry_jaula_fecha = tk.Entry(self.insert_datos)
        self.entry_jaula_fecha.grid(row=11, column=1, pady=pady, padx=padx, sticky="W")
        self.entry_jaula_dias = tk.Entry(self.insert_datos)
        self.entry_jaula_dias.grid(row=12, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_pabellon = ttk.Combobox(self.insert_datos)
        self.combo_pabellon.grid(row=15, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_pabellon["values"], self.id_pab = self.__fill_combo_pabellon()
        self.entry_pabellon_fecha = tk.Entry(self.insert_datos)
        self.entry_pabellon_fecha.grid(row=16, column=1, pady=pady, padx=padx, ipadx=90, sticky="W")

    def __config_button(self):
        pady = 2
        padx = 5

        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.__insertar).grid(row=18, column=1, padx=padx, pady=pady, sticky="W")

    def __insertar(self):  # Insercion en la base de datos.

        vacio1 = ""  # variable para verificar que los tk.Entry no están vacíos
        vacio2 = -1  # variable para verificar que los tk.combobox no están vacíos

        if self.combo_mascota.current() == vacio2:
            self.__popup_error("Se debe seleccionar una mascota ")
        elif self.entry_peso.get() == vacio1:
            self.__popup_error("Se debe ingresar el peso de la mascota")
        elif self.combo_diagnostico.current() == vacio2:
            self.__popup_error("Se debe seleccionar un diagnóstico ")
        elif self.entry_observaciones.get() == vacio1:
            self.__popup_error("Se debe ingresar observaciones ")
        elif self.combo_medico.current() == vacio2:
            self.__popup_error("Se debe seleccionar un diagnóstico ")
        else:
            sql_ser = """insert into servicio(hora, id_mascota, peso) VALUES (now(), %(id_mas)s, %(peso)s) """
            self.db.run_sql(sql_ser, {"id_mas": self.id_masc[self.combo_mascota.current()],
                                      "peso": float(self.entry_peso.get())})


            sql_realiza = """call pr_insert_realizado(%(id_med)s, %(id_diag)s, %(obs)s) """
            self.db.run_sql(sql_realiza, {"id_med": self.id_med[self.combo_medico.current()],
                                          "id_diag": self.id_diag[self.combo_diagnostico.current()],
                                          "obs": self.entry_observaciones.get()})


            self.insert_datos.destroy()

    def __popup_error(self, error):
        tk.messagebox.showerror("Error al ingresar datos", error)


    def __fill_combo_mascota(self):
        sql = "select m.id_mascota, concat(' ',m.nom_masc,',      Dueño: ', nom_due, ' ', ape_due) from mascota m " \
              "join dueno d on m.id_dueno = d.id_dueno;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_medico(self):
        sql = "select id_medico, concat(nom_med, ' ' , ape_med) as nombre from medico;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_diagnostico(self):
        sql = "select id_diag, nom_diag from diagnostico;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_jaula(self):
        sql = "select id_jaula, descripcion from jaula;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_pabellon(self):
        sql = "select id_pabellon, descripcion from pabellon;"
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
        self.entry_fecha = tk.Entry(self.insert_datos)
        self.entry_fecha.place(x=160, y=130, width=200, height=20)
        self.entry_fecha.insert(0, self.row_data[5])

    def config_button(self):  # Botón aceptar, llama a la función modificar cuando es clickeado.
        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.modificar).place(x=50, y=160, width=200, height=20)

    def modificar(self):  # Insercion en la base de datos.

        sql = """update mascota set nom_masc = %(nombre)s, id_especie = %(especie)s,
                    id_dueno = %(dueno)s, descrip_masc = %(descripcion)s, fecha_nacimiento = %(fecha)s where id_mascota = %(id_mascota)s"""
        self.db.run_sql(sql,
                        {"nombre": self.entry_nombre.get(), "especie": int(self.id_esp[self.combo_especie.current()]),
                         "dueno": int(self.id_due[self.combo_dueno.current()]),
                         "descripcion": self.entry_descripcion.get(),
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
