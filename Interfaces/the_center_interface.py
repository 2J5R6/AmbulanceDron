import tkinter as tk
from tkinter import messagebox

def dispatch_drone(emergency_data):
    if not emergency_data:
        messagebox.showinfo("No hay Emergencia", "No se ha reportado ninguna emergencia.")
        return
    messagebox.showinfo("Despacho de Dron", f"Dron despachado a {emergency_data['location']} para {emergency_data['emergency_type']}.")

def start_center_interface(the_center, drone_state_machine, emergency_data):
    center_window = tk.Tk()
    center_window.title('The Center Interface')

    dispatch_button = tk.Button(center_window, text="Dispatch Dron", command=lambda: dispatch_drone(emergency_data))
    dispatch_button.pack()

    center_window.mainloop()
