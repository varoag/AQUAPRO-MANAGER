import tkinter as tk
from tkinter import ttk
from Ejecutable_acuicultura import euler_method


def run_model():
    # Obtener los valores de los campos de entrada
    T_0 = float(T_0_entry.get())
    P_0 = float(P_0_entry.get())
    N_0 = float(N_0_entry.get())
    DBO_0 = float(DBO_0_entry.get())
    DQO_0 = float(DQO_0_entry.get())
    V_0 = float(V_0_entry.get())
    I_0 = float(I_0_entry.get())
    R_0 = float(R_0_entry.get())
    T_ext_0 = float(T_ext_0_entry.get())
    dt = float(dt_entry.get())
    num_steps = int(num_steps_entry.get())
    F_nut = int(F_nut_entry.get())

    # Llamar al método de Euler con los valores ingresados
    T_values, P_values, N_values, DBO_values, DQO_values, V_values, I_values, R_values, T_ext_values = euler_method(T_0, P_0, N_0, DBO_0, DQO_0, V_0, I_0, R_0, T_ext_0, F_nut, dt, num_steps)

    # Realizar cualquier análisis adicional aquí


# Crear la ventana principal
root = tk.Tk()
root.title("AQUAPRO MANAGER V.1.0.")


# Funciones para las opciones del menú
def about():
    tk.messagebox.showinfo("Acerca de", "Interfaz para el Modelo")


# Crear la barra de menú
menu_bar = tk.Menu(root)

# Menú "Archivo"
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Salir", command=root.quit)
menu_bar.add_cascade(label="Archivo", menu=file_menu)

# Menú "Ayuda"
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Acerca de", command=about)
menu_bar.add_cascade(label="Ayuda", menu=help_menu)

root.config(menu=menu_bar)

# Crear y colocar los campos de entrada
inputs_frame = ttk.Frame(root, padding="10")
inputs_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

# Label para indicar las condiciones iniciales
ttk.Label(inputs_frame, text="Condiciones Iniciales").grid(row=0, column=0, columnspan=2, pady=5)

# Parámetros del modelo
parameters = [
    ("Biomasa inicial de plantas (T_0)", 50),
    ("Población inicial de peces (P_0)", 100),
    ("Concentración inicial de nutrientes (N_0)", 50),
    ("Valor inicial de DBO (DBO_0)", 10),
    ("Valor inicial de DQO (DQO_0)", 15),
    ("Volumen inicial de agua (V_0)", 1000),
    ("Intensidad de luz inicial (I_0)", 1000),
    ("Recursos iniciales en el ambiente (R_0)", 50),
    ("Temperatura inicial del ambiente (T_ext_0)", 20),
    ("dt", 0.1),
    ("num_steps", 20),
    ("F_nut", 100)
]

# Crear y colocar campos de entrada para cada parámetro
for i, (param, default_value) in enumerate(parameters, start=1):
    ttk.Label(inputs_frame, text=param + ":").grid(row=i, column=0, sticky=tk.W)
    entry = ttk.Entry(inputs_frame)
    entry.insert(0, str(default_value))
    entry.grid(row=i, column=1)
    globals()[f"{param}_entry"] = entry

# Botones en la barra de herramientas
toolbar = ttk.Frame(root)
toolbar.grid(row=1, column=0, sticky=(tk.W, tk.E))

# Crear un frame para centrar el botón
button_frame = ttk.Frame(toolbar)
button_frame.pack(fill="both")

run_button = ttk.Button(button_frame, text="Ejecutar Modelo", command=run_model)
run_button.pack(pady=5, padx=(10, 10))

# Barra de estado
status_bar = ttk.Label(root, text="Listo", anchor=tk.W)
status_bar.grid(row=2, column=0, sticky=(tk.W, tk.E))

root.mainloop()
