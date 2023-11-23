import tkinter as tk
from tkinter import messagebox
from Interfaces.drone_state_machine_interface import DroneStateMachine

def dispatch_drone(emergency_data):
    if not emergency_data:
        messagebox.showinfo("No hay Emergencia", "No se ha reportado ninguna emergencia.")
        return
    response = messagebox.askokcancel("Despacho de Dron", 
                                      f"Dron despachado a {emergency_data['location']} para {emergency_data['beneficiary_name']}.")
    if response:
        open_drone_interface()

def open_drone_interface():
    # Aquí se abriría la interfaz del dron
    drone_interface = DroneStateMachine()
    # Agregar lógica para mostrar la interfaz del dron

def start_center_interface(the_center, drone_state_machine, emergency_data):
    center_window = tk.Tk()
    center_window.title('The Center Interface')

    # Mostrar datos de la emergencia y botón para despachar el dron
    # Aquí puedes agregar widgets para mostrar los datos de la emergencia
    # ...

    dispatch_button = tk.Button(center_window, text="Dispatch Dron", command=lambda: dispatch_drone(emergency_data))
    dispatch_button.pack()

    center_window.mainloop()
