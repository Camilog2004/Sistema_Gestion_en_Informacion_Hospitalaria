import tkinter as tk
from tkinter import messagebox

from src.gestor_aplicacion.administracion.vacuna import Vacuna
from src.ui_main.gestion.field_frame import FieldFrame


def registrar_vacuna(hospital, frame_implementacion):

    def ver_vacuna_registrada(tipo,nombre,precio):
        #Se limpia el frame
        for item in frame_implementacion.winfo_children():
            item.destroy()

        titulo = tk.Label(frame_implementacion, text="Registrar una vacuna", bg="white", font=("Helvetica", 16, "bold"))
        titulo.pack(pady=20)

        info_vacuna = tk.Label(frame_implementacion, text=f"Informacion de la vacuna registrada", bg="white", font=("Helvetica", 12))
        info_vacuna.pack(pady=10)

        frame_vacuna = tk.Frame(frame_implementacion, bg="white")
        frame_vacuna.pack(padx=10, pady=10)

        label_nombre = tk.Label(frame_vacuna, text="Nombre: ", bg="white", font=("Helvetica", 10, "bold"))
        label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        label_cedula_doctor = tk.Label(frame_vacuna, text=nombre, bg="white")
        label_cedula_doctor.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        label_tipo = tk.Label(frame_vacuna, text="Tipo: ", bg="white", font=("Helvetica", 10, "bold"))
        label_tipo.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        label_tipo = tk.Label(frame_vacuna, text=tipo, bg="white")
        label_tipo.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        label_precio = tk.Label(frame_vacuna, text="Precio: ", bg="white", font=("Helvetica", 10, "bold"))
        label_precio.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        label_precio = tk.Label(frame_vacuna, text=precio, bg="white")
        label_precio.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        #Boton regresar

        from src.ui_main.ventana_principal import implementacion_default

        boton_regresar = tk.Button(frame_implementacion, text="Regresar",
                                   command=lambda: implementacion_default(frame_implementacion))
        boton_regresar.pack(pady=5)


    def crear_vacuna():
        respuesta = tk.messagebox.askyesno("Confirmacion de la vacuna", "¿Estas seguro de agregar esta vacuna?")
        if respuesta:
            nombre = str(fp.getValue(1))
            tipo = str(fp.getValue(2))
            tipo_eps = str(fp.getValue(3)).split(",")
            precio = float(fp.getValue(4))

            vacuna = Vacuna(tipo, nombre, tipo_eps, precio)
            hospital.lista_vacunas.append(vacuna)
            messagebox.showinfo("Vacuna agregada", "La vacuna se ha agregado exitosamente")
            ver_vacuna_registrada(tipo,nombre,precio)


    def borrar_campos():
        for entry in fp.valores:
            entry.delete(0,tk.END)


    # Titulo
    titulo = tk.Label(frame_implementacion, text="Registrar una vacuna", bg="white",font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

    #Formulario

    titulo_ingreso_cedula = tk.Label(frame_implementacion, text="Por favor llene cada uno de los campos:", bg="white",
                                     font=("Helvetica", 10, "bold"))
    titulo_ingreso_cedula.pack(pady=35)

    criterios= ["Nombre de la vacuna", "Ingrese el tipo de vacuna (Obligatoria, No obligatoria)",
                "Ingrese las eps a la que va a pertenecer (Subsidiado, Contributivo, Particular)",
                "Precio"]
    fp =FieldFrame(frame_implementacion,"Criterio", criterios, "Valor", None, None)
    fp.pack()

    #Botones
    botones_frame=tk.Frame(frame_implementacion,bg="white")
    botones_frame.pack(pady=10)


    #Guardar
    boton_guardar_vacuna = tk.Button(botones_frame, text="Guardar", command=crear_vacuna, font=("Helvetica", 10, "bold"))
    boton_guardar_vacuna.grid(row=0, column=0, padx=30, pady=10, sticky="w")

    #Borrar
    boton_borrar = tk.Button(botones_frame, text="Borrar", command=borrar_campos,
                                     font=("Helvetica", 10, "bold"))
    boton_borrar.grid(row=0, column=1, padx=10, pady=30, sticky="w")


    # Funcionalidad para regresar a la ventana principal

    # Se importa aca para evitar una referencia circular
    from src.ui_main.ventana_principal import implementacion_default

    boton_regresar = tk.Button(frame_implementacion, text="Regresar",
                               command=lambda: implementacion_default(frame_implementacion))
    boton_regresar.pack(pady=20)

