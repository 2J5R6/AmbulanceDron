import tkinter as tk
from tkinter import messagebox

def dispatch_drone(emergency_data, center_window, drone_state_machine):
    messagebox.showinfo("Despacho de Dron", f"Dron despachado a {emergency_data['location']} para {emergency_data['beneficiary_name']}.")
    center_window.destroy()
    drone_state_machine.run_interface()

def start_center_interface(the_center, drone_state_machine, emergency_data):
    center_window = tk.Tk()
    center_window.title('The Center Interface')

    if emergency_data:
        tk.Label(center_window, text="Datos de la Emergencia:").pack()
        for key, value in emergency_data.items():
            formatted_text = f"{key.replace('_', ' ').title()}: {value}"
            tk.Label(center_window, text=formatted_text).pack()

    dispatch_button = tk.Button(center_window, text="Dispatch Dron", command=lambda: dispatch_drone(emergency_data, center_window, drone_state_machine))
    dispatch_button.pack()

    center_window.mainloop()
