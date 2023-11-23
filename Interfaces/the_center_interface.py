import tkinter as tk
from tkinter import messagebox
from Interfaces.drone_state_machine_interface import DroneStateMachine

def dispatch_drone(emergency_data, center_window):
    if not emergency_data:
        messagebox.showinfo("No hay Emergencia", "No se ha reportado ninguna emergencia.")
        return
    response = messagebox.askokcancel("Despacho de Dron", 
                                      f"Dron despachado a {emergency_data['location']} para {emergency_data['beneficiary_name']}.")
    if response:
        center_window.destroy()
        open_drone_interface()

def open_drone_interface():
    drone_interface = DroneStateMachine()
    drone_interface.run_interface()  # Asegúrate de que esta función exista en DroneStateMachine

def start_center_interface(the_center, drone_state_machine, emergency_data):
    center_window = tk.Tk()
    center_window.title('The Center Interface')

    # Mostrar datos de la emergencia
    if emergency_data:
        for key, value in emergency_data.items():
            label = tk.Label(center_window, text=f"{key}: {value}")
            label.pack()

    dispatch_button = tk.Button(center_window, text="Dispatch Dron", command=lambda: dispatch_drone(emergency_data, center_window))
    dispatch_button.pack()

    center_window.mainloop()
