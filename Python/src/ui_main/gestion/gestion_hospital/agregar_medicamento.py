from tkinter import messagebox, ttk

from src.gestor_aplicacion.administracion.medicamento import Medicamento
from src.gestor_aplicacion.personas.doctor import Doctor
from src.gestor_aplicacion.personas.enfermedad import Enfermedad
from src.ui_main.gestion.field_frame import FieldFrame
import tkinter as tk


def imprimir_titulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text="Agregar Medicamento", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def agregar_medicamento(hospital, frame):

    def agregar_lista_medicamentos():
        respuesta = tk.messagebox.askyesno("Confirmacion de medicamento", "¿Estas seguro de agregar este medicamento?")

        if respuesta:
            nombre = str(fp.getValue(1))
            descripcion = str(fp.getValue(2))
            cantidad = int(fp.getValue(3))
            precio = float(fp.getValue(4))
            indice_enfermedad = combo_enfermedades.current()
            enf_objeto = Enfermedad.getEnfermedadesRegistradas()[indice_enfermedad]

            medicamento = Medicamento(nombre, enf_objeto, descripcion, cantidad, precio)
            hospital.lista_medicamentos.append(medicamento)
            messagebox.showinfo("Medicamento agregado", "El medicamento se ha agregado exitosamente")
            # Se importa aca para evitar una referencia circular
            from src.ui_main.ventana_principal import implementacion_default
            implementacion_default(frame)
        else:
            messagebox.showinfo("Medicamento no agregado", "No se ha agregado el medicamento")
            # Se importa aca para evitar una referencia circular
            from src.ui_main.ventana_principal import implementacion_default
            implementacion_default(frame)

    def borrar_campos():
        for entry in fp.valores:
            entry.delete(0,tk.END)


    imprimir_titulo(frame)

    criterios = ["Nombre", "Descripcion", "Cantidad", "Precio"]
    fp = FieldFrame(frame, "Criterio", criterios, "Valor", None, None)
    fp.pack()
    enf_frame = tk.Frame(frame, bg="white")
    enf_frame.pack()
    label_enf = tk.Label(enf_frame, text="Enfermedad que trata", bg="white", font=("Helvetica", 10, "bold"))
    label_enf.grid(row=0, column=0, sticky="w")
    combo_enfermedades = ttk.Combobox(enf_frame, values=Enfermedad.getEnfermedadesRegistradas(), state="readonly")
    combo_enfermedades.grid(row=0, column=1, sticky="w")
    boton_agregar = tk.Button(frame, text="Guardar", command=agregar_lista_medicamentos)
    boton_agregar.pack(pady=10)
    boton_borrar = tk.Button(frame, text="Borrar", command=borrar_campos)
    boton_borrar.pack(pady=10)

    # Funcionalidad para regresar a la ventana principal

    # Se importa aca para evitar una referencia circular
    from src.ui_main.ventana_principal import implementacion_default

    boton_regresar = tk.Button(frame, text="Regresar",command=lambda: implementacion_default(frame))
    boton_regresar.pack(pady=10)