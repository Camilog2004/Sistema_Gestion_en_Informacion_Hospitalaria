import tkinter as tk


def asignar_habitacion(hospital, frame_implementacion):
    # Implementacion
    label_inicial = tk.Label(frame_implementacion, text="Asignar habitacion")
    label_inicial.pack()
    label_inicial.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Funcionalidad para regresar a la ventana principal

    # Se importa aca para evitar una referencia circular
    from src.ui_main.ventana_principal import implementacion_default

    boton_regresar = tk.Button(frame_implementacion, text="Regresar",
                               command=lambda: implementacion_default(frame_implementacion))
    boton_regresar.pack()
    boton_regresar.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
import tkinter as tk
from tkinter import ttk, messagebox

from src.gestor_aplicacion.servicios.habitacion import Habitacion

def imprimir_titulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text="Asignar Habitación", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)
def asignar_habitacion(hospital, frame):
    def mostra_asignacion(paciente):
        imprimir_titulo(frame)
        paciente_label = tk.Label(frame, text="Resumen asignación de habitación del Paciente:", bg="white",font=("Helvetica", 12))
        paciente_label.pack(pady=10)
        frame_habitacion=tk.Frame(frame)
        frame_habitacion.pack(fill=tk.BOTH, expand=True)


        cedula_label = tk.Label(frame_habitacion, text=f"Cédula: {paciente.cedula}", bg="white", font=("Helvetica", 10, "bold"))
        cedula_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        nombre_label = tk.Label(frame_habitacion, text=f"Nombre: {paciente.nombre}", bg="white", font=("Helvetica", 10, "bold"))
        nombre_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        numero_label = tk.Label(frame_habitacion, text=f"Número de habitación: {paciente.habitacion_asignada.numero()}", bg="white", font=("Helvetica", 10, "bold"))
        numero_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        categoria_label = tk.Label(frame_habitacion, text=f"Categoría de habitación: {paciente.habitacion_asignada.categoria()}", bg="white", font=("Helvetica", 10, "bold"))
        categoria_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Se importa aca para evitar una referencia circular
        from src.ui_main.ventana_principal import implementacion_default

        boton_regresar = tk.Button(frame_habitacion, text="Regresar", command=lambda: implementacion_default(frame))
        boton_regresar.pack()
    def asignar_habitacion_a_Pacientes(paciente):
        def confirmar_habitacion():
            eleccion = entry.get()
            if eleccion:
                respuesta = tk.messagebox.askyesno("Confirmar habitación", "¿Estas seguro de la elección de esta habitación?")
                if respuesta:
                    numero_habitacion, categoria_habitacion = combo_elegir_habitacion.get().split(" - ")
                    for i, habitacion in enumerate(hospital._habitaciones):
                        if habitacion.numero == numero_habitacion and habitacion.categoria.name == categoria_habitacion:
                            hospital._habitaciones[i].ocupada = True
                            hospital._habitaciones[i].dias = entry.get()
                            hospital._habitaciones[i].paciente = paciente
                            habitacion_nueva = hospital._habitaciones[i]
                            paciente.habitacion_asignada = habitacion_nueva
                            break
                    messagebox.showinfo("Habitación asignada", "La habitación se ha asignado exitosamente")
                    mostra_asignacion(paciente)

                else:
                    messagebox.showinfo("Asignación cancelada", "La asignación de habitación ha sido cancelada")
                    # Se importa aca para evitar una referencia circular
                    from src.ui_main.ventana_principal import implementacion_default
                    implementacion_default(frame)

            else:
                messagebox.showerror("Informacion incompleta",
                                     "Necesita completar todos los espacios para asignar la habitación")

        def obtener_categorias(paciente):
            # Código para obtener las categorías disponibles según la EPS del usuario
            if paciente._tipo_eps == "Subsidiado":
                return ["CAMILLA", "OBSERVACION", "UCI"]
            elif paciente._tipo_eps == "Contributivo":
                return ["INDIVIDUAL", "DOBLE", "OBSERVACION", "UCI", "UCC"]
            else:
                return ["CAMILLA", "UCI"]

        def obtener_habitaciones(categoria):
            # Código para obtener las habitaciones disponibles para la categoría seleccionada.
            habitaciones_disponibles = Habitacion.buscar_habitacion_disponible(categoria)
            if habitaciones_disponibles:
                return habitaciones_disponibles


        imprimir_titulo(frame)

        info_paciente = tk.Label(frame, text=f"{paciente.nombre} - CC: {paciente.cedula}", bg="white", font=("Helvetica", 12))
        info_paciente.pack(pady=10)

        frame1 = tk.Frame(frame, bg="white")
        frame1.pack()

        def limpiar_entry():
            entry.delete("0", "end")

        def habilitar_elegir_habitacion(event):
            eleccion = combo_tipo_categoria.get()
            combo_elegir_habitacion.set("")
            limpiar_entry()
            entry.config(state='disabled')
            if eleccion:
                habitaciones_disponibles = obtener_habitaciones(eleccion)
                if habitaciones_disponibles:
                    combo_elegir_habitacion['state'] = 'readonly'
                    combo_elegir_habitacion['values'] = [f"{habitacion.numero} - {habitacion.categoria.name}" for habitacion in habitaciones_disponibles]
                else:
                    # No hay habitaciones disponibles para la categoría seleccionada
                    respuesta = messagebox.askquestion("No hay habitaciones disponibles",
                                                       "No hay habitaciones disponibles para la categoría seleccionada. ¿Desea cambiar de categoría a una inferior?")
                    if respuesta == 'yes':
                        # Aquí puedes implementar la lógica para cambiar la categoría
                        nueva_categoria = Habitacion.buscar_otra_categoria(combo_tipo_categoria.get())  # Función para obtener la nueva categoría
                        if nueva_categoria:
                            combo_tipo_categoria.set(str(nueva_categoria))  # Establecer la nueva categoría en el Combobox
                            habilitar_elegir_habitacion(None)  # Llamar nuevamente a la función para habilitar las habitaciones

                    else:

                        combo_elegir_habitacion['state'] = 'disabled'
            else:
                combo_elegir_habitacion['state'] = 'disabled'

        def habilitar_ingresar_dias(event):
            eleccion = combo_elegir_habitacion.get()
            limpiar_entry()
            if eleccion:
                entry.config(state='normal')
                entry.update()  # Agregar esta línea para actualizar el estado del Entry
            else:
                entry.config(state='disabled')
                limpiar_entry()

        tipo_categoria = tk.Label(frame1, text="Seleccione el tipo de categoria:", bg="white", font=("Helvetica", 10, "bold"))
        tipo_categoria.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        valor_defecto1 = tk.StringVar()
        combo_tipo_categoria = ttk.Combobox(frame1, values=obtener_categorias(paciente),
                                       textvariable=valor_defecto1, state="readonly")
        combo_tipo_categoria.bind("<<ComboboxSelected>>", habilitar_elegir_habitacion)
        combo_tipo_categoria.grid(row=0, column=1, padx=10, pady=10, sticky="w")


        elegir_habitacion = tk.Label(frame1, text="Seleccione la habitación de su preferencia:", bg="white", font=("Helvetica", 10, "bold"))
        elegir_habitacion.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        valor_defecto2 = tk.StringVar()
        combo_elegir_habitacion = ttk.Combobox(frame1, textvariable=valor_defecto2, state="disabled")
        combo_elegir_habitacion.bind("<<ComboboxSelected>>", habilitar_ingresar_dias)
        combo_elegir_habitacion.grid(row=1, column=1, padx=10, pady=10, sticky="w")



        label_entry = tk.Label(frame1, text="Ingrese los dias:", bg="white", font=("Helvetica", 10, "bold"))
        label_entry.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        entry = tk.Entry(frame1, state='disabled')
        entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")


        boton_aceptar = tk.Button(frame, text="Aceptar", command=confirmar_habitacion)
        boton_aceptar.pack(pady=5)

        # Se importa aca para evitar una referencia circular
        from src.ui_main.ventana_principal import implementacion_default

        boton_regresar = tk.Button(frame, text="Regresar", command=lambda: implementacion_default(frame))
        boton_regresar.pack(pady=5)

    def buscar_paciente():
        cedula = ingreso_cedula.get()
        paciente = hospital.buscar_paciente(int(cedula))

        # Continua si el paciente esta registrado en el hospital
        if paciente is not None:
            asignar_habitacion_a_Pacientes(paciente)
        else:
            respuesta = tk.messagebox.askyesno("Error", "No existe un paciente registrado con esta cedula. "
                                                        "¿Desea intentar de nuevo?")
            if not respuesta:
                # Se importa aca para evitar una referencia circular
                from src.ui_main.ventana_principal import implementacion_default
                implementacion_default(frame)

    imprimir_titulo(frame)

    # Pide la cedula del paciente
    label_ingreso_cedula = tk.Label(frame, text="Ingrese la cédula del paciente:", bg="white",
                                    font=("Helvetica", 10, "bold"))
    label_ingreso_cedula.pack()

    ingreso_cedula = tk.Entry(frame)
    ingreso_cedula.pack(pady=5)

    boton_buscar_paciente = tk.Button(frame, text="Buscar", command=buscar_paciente)
    boton_buscar_paciente.pack(pady=10)

    # Funcionalidad para regresar a la ventana principal

    # Se importa aca para evitar una referencia circular
    from src.ui_main.ventana_principal import implementacion_default

    boton_regresar = tk.Button(frame, text="Regresar",
                               command=lambda: implementacion_default(frame))
    boton_regresar.pack()
